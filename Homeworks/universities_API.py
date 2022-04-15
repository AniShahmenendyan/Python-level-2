from flask import request
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
def get_universities():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }

    url = "https://cwur.org/2021-22.php"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_html = response.text
        soup = BeautifulSoup(response_html, 'html.parser')
        university_list_div = soup.find('div', {'class': 'table-responsive'}).find_all('td')

        universities_list = []

        for val in university_list_div:
            universities_list.append(val.text)

        universities = []
        for i in range(0, len(universities_list) - 9, 9):
            universities.append({'rank': universities_list[i], 'name': universities_list[i + 1],
                                 'country': universities_list[i + 2],
                                 'score': universities_list[i + 8]})

        return universities
data = get_universities()


class University(db.Model):
    __tablename__ = "universities"
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Numeric(1, 1), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

def add_universities():
    for item in data:
        rank = item["rank"]
        name = item["name"]
        country = item["country"]
        score = item["score"]
        uni = University(rank=rank, name=name, country=country, score=score)

        db.session.add(uni)
        db.session.commit()


@app.route('/')
def home():
    page = "1"
    if request.args.get("page"):
        page = request.args.get('page')
    if request.args.get('country'):
        cnt = request.args.get('country')
        all_data = University.query.filter_by(country=cnt).offset((int(page)-1) * 20).limit(20).all()
        d = [{'name': datas.name, 'country': datas.country} for datas in all_data]
        return jsonify(d)
    all_data = University.query.offset((int(page) - 1) * 20).limit(20).all()
    d = [{'name': datas.name, 'country': datas.country} for datas in all_data]
    return jsonify(d)
