import os
import argparse
import logging
import datetime
# import pytz
from db.tools.create_table import DbBuilder
from db.tools.db_sqlite import DB
from sub_process import assistant
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


obj = ServiceChooser()
obj.create_db()
# database = DB('db/database.db')
# db = DbBuilder(database)
