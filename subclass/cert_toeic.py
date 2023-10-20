import requests
from bs4 import BeautifulSoup

URL = "https://exam.toeic.co.kr/receipt/examSchList.php"

response = requests.get(URL)

del_list = [" ", "\n", "\t", "★", "정기접수:", "특별추가:", "접수예정", "접수하기"]

bef_list = ["회2","분2","시202","시제"]

aft_list = ["회 2","분 2","시 202","시 제"]

final_toeic = []

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    ori = soup.select_one("#contents > div > div.table_data > table > tbody")

    ori = ori.get_text()

    for v in range(len(del_list)):
        ori = ori.replace(del_list[v], '')

    for r in range(len(bef_list)):
        ori = ori.replace(bef_list[r], aft_list[r])

    com = ori.split(" ")

    for i in range(int((len(com)/5))):
        child_list = [com[0+(5*i)], com[1+(5*i)], com[2+(5*i)], com[3+(5*i)], com[4+(5*i)]]
        final_toeic.append(child_list)

    # 0, 5, 10 ... 회차
    # 1, 6, 11 ... 시험일시
    # 2, 7, 12 ... 성적발표일시
    # 3, 8, 13 ... 정기 접수 기간
    # 4, 9, 14 ... 특별 추가 접수 기간
