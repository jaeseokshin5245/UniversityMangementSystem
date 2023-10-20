
import requests
import bs4
import pandas as pd
decoding = "AMafFXacwPEEttxqQmGu3AYOxqPJlHjhEOFKzWtEukXCvbVj4WLX5jid9bORmlmD5VWvU9Upll6zUJT8fflI9w=="
# encoding = "AMafFXacwPEEttxqQmGu3AYOxqPJlHjhEOFKzWtEukXCvbVj4WLX5jid9bORmlmD5VWvU9Upll6zUJT8fflI9w%3D%3D"

url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getEList'

params = {'serviceKey' : decoding}
response = requests.get(url, params=params)

content = response.text

xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
rows = xml_obj.findAll('item')

# 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
row_list = [] # 행값
name_list = [] # 열이름값
value_list = [] #데이터값

for i in range(0, len(rows)):
    columns = rows[i].find_all()

    for j in range(0,len(columns)):
        if i == 0:

            name_list.append(columns[j].name)
        value_list.append(columns[j].text)

    row_list.append(value_list)
    value_list=[]

cert_df = pd.DataFrame(row_list, columns=name_list)
cert_list = cert_df.values.tolist()
