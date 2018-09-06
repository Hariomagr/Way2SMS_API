__author__ = "Hariom Agrawal"
__copyright__ = "Copyright (C) 2018 Hariom Agrawal"
__license__ = "Public Domain"
__version__ = "1.0"
#Use this code at your own risk#
#Enter registered mobile number and password in the data dictionary 
#Enter Message in data1 dictionary and enter mobile number in which message needs to be sent in toMobile in data1.

import requests
from bs4 import BeautifulSoup
url1='http://www.way2sms.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
s=requests.session()
url=s.get(url1,headers=headers,verify=False)
data={
    'mobileNo':'Enter registered mobile number',
    'password':'Enter password here',
    'CatType':''
}
url=s.post('http://www.way2sms.com/re-login',data=data,headers=headers,verify=False)
url=s.post(url1+'send-sms',data=data,headers=headers,verify=False)
x=s.cookies.get_dict()['JSESSIONID']
x=x.split('~')[1]
data1={
    'Token':x,
    'message':'Enter Message Here',
    'toMobile':'Enter to mobile number',
    'ssaction':'undefined'
}
url=s.post(url1+'smstoss',data=data1,headers=headers,verify=False)
