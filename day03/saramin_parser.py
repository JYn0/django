from bs4 import BeautifulSoup
import requests

url = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404&panel_type=&search_optional_item=n&search_done=y&panel_count=y"

response = requests.get(url)
# print(response)
# print(response.text)

html = BeautifulSoup(response.text, 'html.parser')

'''
# company_name class 찾기
company_names = html.select('.company_name')
recruit_names = html.select('.recruit_name')
recruit_conditions = html.select('.list_recruit_condition')

for company_name,recruit_name, condition in zip(company_names, recruit_names, recruit_conditions):
    print(f'{company_name.text}- {recruit_name.text}')
    print(condition.text)
'''
'''
for company_name in company_names:
    # print(company_name)
    print(company_name.text)
for recruit_name in recruit_names:
    print(recruit_name.text)
print(len(company_names))
print(len(recruit_names))
'''
# 위에 두개 주석부분 내용과 동일
company = html.select('.part_top')
for com in company:
    print(f'{com.select_one(".company_name").text}- {com.select_one(".recruit_name").text}')
    print(com.select_one('.list_recruit_condition').text)
    break


# 2차 크롤링
company_list = html.select('ul.product_list li') # product_list 안에 있는 li
for com in company_list:
    # a tag 한번 더 찾기, href 속성 값
    idx = com.select_one('a')['href'].split('=')[-1]
    company_info_url = 'http://www.saramin.co.kr/zf_user/jobs/relay/view-ajax'
    company_info_params = { 'rec_idx': idx }
    company_response = requests.post(company_info_url, params=company_info_params)
    print(company_response)
    company_html = BeautifulSoup(company_response.text, 'html.parser')
    company_title = company_html.select_one('a.company').text
    print(company_title.strip())

    break



# my_query
# dictionary에 all, position 나눠서 넣고 url에 넣어서 요청하기
'''
my_query = {
    'All' : {
        'name': 'cat_cd',
        'webAll': '404'
    },
    'position': {
        'name': 'cat_key',
        'IOS': '40701'
    }
}

my_url = f'http://www.saramin.co.kr/zf_user/jobs/list/job-category?{my_query["All"]["name"]}={my_query["All"]["webAll"]}&panel_type=&search_optional_item=n&search_done=y&panel_count=y'
my_response = requests.get(my_url)
my_html = BeautifulSoup(my_response.text, 'html.parser')
my_company = my_html.select('.part_top')
for my_com in my_company:
    print(f"{my_com.select_one('.company_name').text}- {my_com.select_one('.recruit_name').text}")
    print(my_com.select_one('.list_recruit_condition').text)
'''
