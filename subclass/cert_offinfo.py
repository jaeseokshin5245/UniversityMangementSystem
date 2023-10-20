import requests
from bs4 import BeautifulSoup


URL  = "https://www.historyexam.go.kr/pageLink.do?link=examSchedule&netfunnel_key=F0BDE89FC56F54A6702B2A26698B840AC10BD9979C71387AAC2DD6B3E84FB7C7C29BE43E2F06D1CC2132FFF608CCD24ABAF809D04A3401E133AF9A30902377E83821E17F843D34378BA94467ADC88BA74B16061CE3A7838A42C123D251D01EACA6473F2826BD6E38AB7A4693F370CC97302C382C312C302C30"

response = requests.get(URL)

del_list = [" ", "\n", "\t"]

final_toeic = []

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    ori = soup.select_one("#sub_content > div.right_sider > div.right_contents > table:nth-child(3) > tbody")

    ori = ori.get_text()

    ori = ori.replace("\n", '')

    # 0, 5, 10 ... 회차