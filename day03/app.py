from flask import Flask, request, render_template
import requests

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    # request.args.get('파라미터명')
    # request.args -> flask가 client로부터 받은 파라미터를 담는 Dictionary(Immutable)
    student = request.args.get('student')
    return {'hello': student}
'''
# 주소 자체에 parameter 심어놓기
@app.route('/<day>')
def toons(day):
    return{ 'today is': day}
'''

@app.route('/daum_webtoon')
def daum_toon_index():
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    msg = "아... 집가고싶다"
    msg2 = "배고프다"
    # **locals() -> 값 넘겨주기
    # days=days -> days만 넘겨주기 원하는 데이터만 template에 넘겨주기, 여러개 보낼 수 있음
    return render_template('daum_webtoon_list.html', days=days, msg=msg)
# http://localhost:5000/daum_webtoon


@app.route('/daum_webtoon/<day>')
def daum_toon(day):
    url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
    data = request_json_data_from_url(url)
    return { day: parse_daum_webtoon_data(data)}

def request_json_data_from_url(url):
    response = requests.get(url)
    data = response.json()
    return data

def parse_daum_webtoon_data(data):
    # data parsing
    toons = []
    for toon in data["data"]:
        title = toon["title"]

        desc = toon["introduction"]

        genres = []
        for genre in toon["cartoon"]["genres"]:
            genres.append(genre["name"])

        artists = []
        for artist in toon["cartoon"]["artists"]:
            artists.append(artist["name"])
        
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
    return toons

# http://localhost:5000/daum_webtoon/mon