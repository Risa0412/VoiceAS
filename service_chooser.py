# -*- coding: utf-8 -*-
import os
import argparse
import logging
import datetime
import webbrowser
# import pytz
from db.tools.create_table import DbBuilder
from db.tools.db_sqlite import DB
from interface.voice.sub_process import assistant
from modules.web_scraping.case_cookpad.builder import Builder
# import subprocess

class ServiceChooser: 
    def __init__(self):
        self.db_path = os.path.join(os.getcwd(), 'db/database.db')

    def create_db(self):
        database = DB(self.db_path)
        db = DbBuilder(database)

    def get_time(self):
        assistant('時間')
        # subprocess.call('python sub_process.py -r 時間')

    def get_page(self):
        bu = Builder()
        url = 'https://cookpad.com/search/パスタ'
        self.data = bu.get_data(url)# ディクショナリ型で返ってくる。
        # lst = []
        # for key in data.keys():
        #     lst.append(key)
        self.lst = [key for key in self.data.keys()]

        # print(lst)
        # user_choice = 3
        # print(data[lst[user_choice-1]])

    def tester(self):
        self.get_page()# レシピの表示
        print(self.lst)
        user = input('どんなレシピが見たいですか？\n')
        try:
            user = int(user)
            while user > len(self.lst):
                if user <= len(self.lst):
                    url = 'https://cookpad.com' + self.data[self.lst[user-1]]# 選んだ料理名のクックパッドのページのURLを作成。self.data[料理名] = recipeのID
                # user = input('どんなレシピが見たいですか？\n')
                '''recusive'''

        except ValueError:
            url = 'https://cookpad.com' + self.data[user]# 選んだ料理名のクックパッドのページのURLを作成。self.data[料理名] = recipeのID
        webbrowser.open(url)



obj = ServiceChooser()
# obj.create_db()
# obj.get_page()
# database = DB('db/database.db')
# db = DbBuilder(database)
obj.tester()