import csv

from bs4 import BeautifulSoup
import requests
import json

from django.core.management import BaseCommand

from quote.models import Author, Quote, Tag

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}

url = "https://quotes.toscrape.com/page/"


class Command(BaseCommand):
    help = 'Scraping quotes from url and import to db.'

    def handle(self, *args, **options):
        datas = self.extract_data(10)

        for data in datas:
            author, is_created = Author.objects.get_or_create(name=data['author'])
            quote = Quote(text=data['quote'], author=author)
            quote.save()
            tags = set()
            for tag in data['tags']:
                try:
                    tags.add(tag)
                    tag = Tag(name=tag)
                    tag.save()
                    quote.tag.add(tag)
                except Exception as e:
                    pass


    @staticmethod
    def extract_data(total_pages):
        global authors_list, quotes_list, tags_list, quotes
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }
        url = "https://quotes.toscrape.com/page/"
        response_html = ''
        for page_number in range(1, total_pages + 1):

            response = requests.get(url + str(page_number), headers=headers)

            if response.status_code == 200:
                response_html += response.text
                soup = BeautifulSoup(response_html, 'html.parser')
                scrap = soup.find_all('div', {'class': 'quote'})

                quotes_scrap = soup.find_all('span', {'class': 'text'})
                quotes_list = []
                for quote in quotes_scrap:
                    quotes_list.append(quote.text)

                tags_scrap = soup.find_all('meta')
                tags_list = []
                for tag in tags_scrap:
                    if tag.get("content"):
                        tags_list.append(tag.get("content").split(','))
                    else:
                        tags_list.append([])
                i = 0
                while i < len(tags_list):
                    tags_list.pop(i)
                    i += 10

                authors_scrap = soup.find_all('small', {'class': 'author'})

                authors_list = []
                for author in authors_scrap:
                    authors_list.append(author.text)
            quotes = []

            for i in range(len(quotes_list)):
                quotes.append(dict(quote=quotes_list[i], author=authors_list[i], tags=tags_list[i]))

        return quotes
