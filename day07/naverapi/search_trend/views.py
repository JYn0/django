from django.shortcuts import render
import json
import requests

# Create your views here.
def search(request):
    # 검색어를 입력하는 곳
    return render(request,'search.html')

def result(request):
    # 검색어에 대한 검색 트렌드를 받아보는 곳
    start_date = request.GET['search_start_date']
    end_date = request.GET['search_end_date']
    time_unit = request.GET['search_time_unit']
    group_name = request.GET['search_group_name']
    keywords = request.GET['search_keywords'].split(',')

    query = {
        "startDate": start_date,
        "endDate": end_date,
        "timeUnit": time_unit,
        "keywordGroups": [
          {
            "groupName": group_name,
            "keywords": keywords
          }
        ]
    }

    
    url = 'https://openapi.naver.com/v1/datalab/search'
    client_id = 'key'
    client_secret = 'secret'

    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    params = json.dumps(query) # dictionary to JSON

    response = requests.post(url, headers=headers, data=params)
    # POST방식은 url, headers, data를 보내야함
    result = response.text

    context = {
        'result': result
        # 'result': {
        #     'start_date': start_date,
        #     'end_date': end_date,
        #     'time_unit': time_unit,
        #     'group_name': group_name,
        #     'keywords': keywords
        # }
    }

    return render(request,'result.html', context)