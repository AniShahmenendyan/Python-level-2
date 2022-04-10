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
    with open('../web/universities.csv', 'w') as file:
        file.write(response_html)
        soup = BeautifulSoup(response_html, 'html.parser')



university_list_div = soup.find('div', {'class': 'table-responsive'})
university_name_list = university_list_div.find_all('a')
universities_list = []
for name in university_name_list:
    universities_list.append(name.text)
i = 1
while  i < len(universities_list):
    universities_list.pop(i)
    i += 1
print(universities_list)

with open('../web/universities.json', 'w') as f:
    f.write(json.dumps(universities_list, ensure_ascii=False))
