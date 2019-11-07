import random

import json
import requests
import time

# {ditionary}, Key:Value
student_phone_number = {
    "이름": "010-0000-0000"
}
# 변수명["Key"]
'''
student_phone_number["이름"]
print(student_phone_number["이름"])     # 010-0000-0000
print(student_phone_number.get("이름")) # 010-0000-0000
'''

lunch_menu = {
    "20층 식당": {
        "A코스": "돈까스",
        "B코스": "순대국"
    },
    "양자강": {
        "점심메뉴": "탕짬면",
        "특선메뉴": "군만두"
    },
    "대동집": {
        "밥안주": "비빔면",
        "술안주": "오돌뼈"
    }
}
'''
print(lunch_menu["20층 식당"]["B코스"])         # 순대국
print(lunch_menu.get("20층 식당").get("B코스")) # 순대국
'''
# 딕셔너리에 새로운 데이터 추가하기
lunch_menu["경성불백"] = {
    "한식메뉴": "석쇠불고기",
    "특식": "돈까스"
}
'''
print(lunch_menu)
lunch_menu["양자강"] = "짜장면"
print(lunch_menu)
'''

'''
print(lunch_menu)
# 모든 key값 뽑기
print(lunch_menu.keys())
# 모든 value값 뽑기
print(lunch_menu.values())
# 모든 값 뽑기
print(lunch_menu.items())
'''

'''
# 한번 순회할 때 마다 data를 담아놓는 임시변수 -> a
#  순회를 하려는 대상 keys, values, items -> b
# for a in b
for key in lunch_menu.keys():
    print(key)
for value in lunch_menu.values():
    print(value)
for key, value in lunch_menu.items():
    print(key, value)
'''
'''
# 여러개중에 choice 한개, sample 여러개 중에 n개
print(random.choice(list(lunch_menu.keys())))
print(random.sample(list(lunch_menu.keys()), 2))
'''

# 3번

url = "http://webtoon.daum.net/data/pc/webtoon/list_serialized/fri"

# print(data)
# print(type(data))

# for d in data.keys():
#     print(d)
#print(type(data["data"])) # list
# webtoon_data = data["data"]

# 3-1


'''
def 함수명(파라미터):
    함수만들기
'''

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


days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
daily_toon_data = {}

for day in days:
    print(day)
    url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
    data = request_json_data_from_url(url)
    daily_toon_data[day] = parse_daum_webtoon_data(data)
    print(daily_toon_data[day])
    time.sleep(3)
  