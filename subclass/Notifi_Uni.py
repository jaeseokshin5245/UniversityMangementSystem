import requests
from bs4 import BeautifulSoup

URL = "https://www.wsu.ac.kr/board/index.jsp?code=community0101"

''' 공지 리스트 페이지 URL '''

front_url = 'https://www.wsu.ac.kr/board/'

''' 공지 URL에 앞부분에 해당하는 문자열 '''

def latest_uni_noti():
    ''' 가장 최신'''
    response = requests.get(URL)
    ''' URL로부터 html 요청 '''

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        ori = str(soup.select_one('#board > div.board-list > ul > li:nth-child(11) > h4 > span:nth-child(1) > a'))

        ori = ori.split('"', 4)

        prec = ori[3]

        back_url = prec.replace('amp;' , '')
        ''' pre_3의 amp; 문자열을 삭제(실제로는 ''으로 치환한 것으로 수행)하고 back_url에 대입'''

        full_url = front_url + back_url
        ''' front_url과 back_url 문자열을 합침'''

        result_url = full_url.replace('"', '')       
        ''' back_url에 남아있던 큰 따옴표(")를 제거하고 result_url에 대입'''
    else : 
        ''' 상태 코드가 200(성공)이 아닌 상황(== 실패)이면 아래 코드 진행 '''

        print(response.status_code)
        ''' 그 반응에 해당하는 상태 코드 출력 '''
        ''' ex) 해당 서버 없음 -> 404 '''

    response = requests.get(result_url)
    ''' 가장 최신 공지에 해당하는 URL로 부터 html 요청 '''

    if response.status_code == 200:
        '''요청 받은 상태 코드가 200(성공)이면 아래 코드 진행'''

        soup = BeautifulSoup(response.text, 'html.parser')
        ''' --전략-- '''

        mol_lu = soup.select_one('#board > div > div.board-body > div.board-webzine > div.view_editor')
        ''' 공지 내용에 해당하는 html 부분의 내용을 soup를 통해 가져와서 mol_lu 변수에 대입'''

        eva = mol_lu.get_text()
        ''' mol_lu에 해당하는 내용들에서 태그 값을 모두 뺀 텍스트만 남기고 eva 변수에 대입'''

        clear_eva = eva.replace(' ', '')
        ''' 출력 값의 줄간격이 너무 넓어 줄바꿈(/n)에 해당하는 값을을 모두 제거하고 clear_eva에 대입'''
        
        return clear_eva
        '''함수 리턴값을 clear_eva로 지정'''

    else:
        print(response.status_code)
        ''' -전략- '''

late_uni_noti = latest_uni_noti()
'''latest_uni_noti를 late_uni_noti로 대입
    여기서는 리턴값인 clear_eva의 값이 late_uni_noti로 대입 됨.'''