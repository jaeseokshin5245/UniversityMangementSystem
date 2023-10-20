import json
from urllib import request
import urllib.parse
from parse import *
from datetime import datetime
# from band_post import Post
LIST_URL = f'https://openapi.band.us/v2/band/posts'
LAST_URL = 'https://openapi.band.us/v2.1/band/post'
TOKEN = "ZQAAAXXq6KecZDSFF6I1y0hRZmShv91jd4l8I-VbGx74lm0ibl2uAvmEWLrBMrSAdoqdoUz9GeJeQ_fP7QXaWuDCpwlmbeNEhxfm7EjjE1l_x-rS"
BAND_KEY = 'AAAg3Y7Bca6p-Xonheibs9tP'

class Find_lastest:
    def get_lastest_token(self):
        def process_dict(data, req):
                inquiry_list_data = urllib.parse.urlencode(data).encode('utf-8')
                res = request.urlopen(req, inquiry_list_data)
                decoded = res.read().decode("UTF-8")
                json_dict = json.loads(decoded)      
                return json_dict

        list_req = request.Request(LIST_URL)
        list_data = {'access_token': TOKEN, 'band_key' : BAND_KEY, 'locale' : 'ko_KR'}
        list_token = process_dict(list_data, list_req)

        late_post_key = list_token['result_data']['items'][0]['post_key']

        last_req = request.Request(LAST_URL)
        last_data = {'access_token': TOKEN, 'band_key' : BAND_KEY, 'post_key' : late_post_key}
        last_token = process_dict(last_data, last_req)

        return last_token

class Post:
    def __init__(self, response) -> None:
        self._name = ""
        self._created_at = 0
        self._content = ""

        self.from_response(response)
    
    def from_response(self, response):
        try:
            self._name = response['result_data']['post']['author']['name']
            self._created_at = response['result_data']['post']['created_at']
            self._content = response['result_data']['post']['content']
        except:
            pass

    @property
    def name(self):
        return self._name

    @property
    def content(self):
        return self._content

    @property
    def created_at(self):
        return datetime.fromtimestamp(int(self._created_at/1000))


find_C = Find_lastest()
# obj = Post_class(post_inquiry_detail_bands(find_obj.get_lastest_token()))
obj = Post(find_C.get_lastest_token())

author, content  = obj.name ,obj.content
post_time = str(obj.created_at)
uni_notfi = author+ "\n" + post_time + "\n" + content 

# print(uni_notfi)
# # Completed!

