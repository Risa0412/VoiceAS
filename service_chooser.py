import os
import argparse
import logging
import datetime
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
        data = bu.get_data(url)
        # lst = []
        # for key in data.keys():
        #     lst.append(key)
        lst = [key for key in data.keys()]

        print(lst)
        user_choice = 3
        print(data[lst[user_choice-1]])


obj = ServiceChooser()
# obj.create_db()
obj.get_page()
# database = DB('db/database.db')
# db = DbBuilder(database)
