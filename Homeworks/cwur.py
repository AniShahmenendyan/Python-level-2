from bs4 import BeautifulSoup
import requests
import json

headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}



url = "https://cwur.org/2021-22.php"
response = requests.get(url, headers=headers)
if response.status_code == 200:
    response_html = response.text
    # with open('../web/universities.csv', 'w') as file:
    #     file.write(response_html)
    soup = BeautifulSoup(response_html, 'html.parser')




university_list_div = soup.find('div', {'class': 'table-responsive'}).find_all('td')
# print(university_list_div)
universities_list = []

for val in university_list_div:
    universities_list.append(val.text)
# print(universities_list)
universities = []
for i in range(0, len(universities_list)-9, 9):
    universities.append({'id': universities_list[i], 'name': universities_list[i + 1],
                        'country': universities_list[i + 2],
                        'score': universities_list[i+8]})


with open('../web/universities.json', 'w') as f:
    f.write(json.dumps(universities, ensure_ascii=False))
