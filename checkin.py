import sys
import requests
from os import getenv

username = getenv('USERNAME')
password = getenv('PASSWORD')
TGCHATID = getenv('TGCHATID')
BOTTOKEN = getenv('BOTTOKEN')
Url = getenv('URL')

session = requests.session()
session.get(Url)

LoginUrl = Url + '/auth/login'
LoginHeaders = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
}
LoginData = {
    'email': username,
    'passwd': password
}
rLogin = session.post(url = LoginUrl, data = LoginData, headers = LoginHeaders)

CheckUrl = Url + '/user/checkin'
CheckHeaders = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
rCheck = session.post(url = CheckUrl, headers = CheckHeaders)
str = rCheck.content
str1 = rCheck.text
print(str)
print(str1)
