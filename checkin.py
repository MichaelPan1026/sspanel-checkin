import sys
import cfscrape
from os import getenv

username = getenv('USERNAME')
password = getenv('PASSWORD')
TGCHATID = getenv('TGCHATID')
BOTTOKEN = getenv('BOTTOKEN')
Url = getenv('URL')

scraper = cfscrape.create_scraper()
scraper.get(Url)

LoginUrl = Url + '/auth/login'
LoginHeaders = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
}
LoginData = {
    'email': username,
    'passwd': password
}
rLogin = scraper.post(url = LoginUrl, data = LoginData, headers = LoginHeaders)

if rLogin.headers['content-length'] == '42' :
    print('机场登陆成功')
    CheckUrl = Url + '/user/checkin'
    CheckHeaders = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
    rCheck = scraper.post(url = CheckUrl, headers = CheckHeaders)
    str = rCheck.content.decode('utf-8').split("\"")[5].encode('utf8').decode('unicode_escape')
    print(str)
    TelegramPush = 'https://api.telegram.org/bot' + BOTTOKEN + '/sendMessage?chat_id=' + TGCHATID + '&text=' + str
    rPush = scraper.get(TelegramPush)
    if rPush.status_code == 200 :
        print('推送成功')
    elif rPush.status_code == 400 :
        print('CHATID 填写有误')
    else :
        print('推送失败，未知错误')
else:
    print('机场登陆失败')
    sys.exit(1)
