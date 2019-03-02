#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import itchat
import time
import math
import datetime

START_TIME = "2019-3-2 17:00:30"
INTERVAL = 3600

class WeBot(object):
    def __init__(self):
        itchat.auto_login(enableCmdQR=2, hotReload=True)
        self.USERNAME_KEY = 'UserName'

    def send(self, message, user_remark_name):
        user = itchat.search_friends(remarkName=user_remark_name)
        itchat.send(message, user[0][self.USERNAME_KEY])

if __name__ == '__main__':
    bot = WeBot()

    now = datetime.datetime.now()
    schedule_time = datetime.datetime.strptime(START_TIME, "%Y-%m-%d \
    %H:%M:%S")

    next_time_interval = (datetime.timedelta(seconds=max(0, \
        math.ceil((now - schedule_time).total_seconds() / INTERVAL)) * INTERVAL) + \
        schedule_time - now).total_seconds()

    time.sleep(next_time_interval)
    count = 1
    while True:
        bot.send(str(count), 'Bot')
        count += 1
        time.sleep(INTERVAL)
