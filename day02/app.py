from flask import Flask, escape, request
import json
import requests

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)
# $env:FLASK_ENV="Develpment"
# $env:FLASK_DEBUG="Develpment"
@app.route('/')
def index():
    daily_toon_data = {}
    day = 'mon'
    url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
    data = request_json_data_from_url(url)
    daily_toon_data[day] = parse_daum_webtoon_data(data)
    # print(daily_toon_data[day])
    
    return daily_toon_data


def request_json_data_from_url(url):
    # data 크롤링
    # 해당 url에 요청 보내기
    response = requests.get(url)
    data = response.json()
    return data

def parse_daum_webtoon_data(data):
    # data parsing
    toons = []
    for toon in data["data"]:
        # 제목의 key는 'title'
        title = toon["title"]

        # 설명의 key는 'introduction'
        desc = toon["introduction"]

        # 장르의 위치는 'cartoon'안에 'genre'리스트 안에 'name' key
        genres = []
        for genre in toon["cartoon"]["genres"]:
            genres.append(genre["name"])
        # print(genres)

        # 작가의 위치는 'cartoon'안에 'artists'리스트 안에 'name' key
        artists = []
        for artist in toon["cartoon"]["artists"]:
            artists.append(artist["name"])
        # print(name)
        
        # 썸네일 이미지의 위치는 'pcThumbnailImage'리스트 안에 'url'key
        img_url = toon["pcThumbnailImage"]["url"]
        tmp = {
            title:{
                "desc":desc,
                "writer":artists,
                "genres":genres,
                "img_url":img_url
            }
        }
        toons.append(tmp)
        # print(toons)
    return toons