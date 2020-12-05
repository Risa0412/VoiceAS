# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("../..")
from tools.importer_saver import from_json
from db.tools.db_sqlite import DB

# TODO deplace in populate_db
class DbBuilder:
    def __init__(self, db):
        # self.sql_db = DB('../database.db')
        self.sql_db = db
        self.create_base_tables()

    def create_base_tables(self):
        """
        Set the base tables sql syntax
        :return:
        """
        PATH = 'db/base_tables'
        f = []
        for (dirpath, dirnames, filenames) in os.walk(PATH):
            f.extend(filenames)
            break

        for files in f:
            if '.json' in files:
                base_tables = from_json(PATH, files)
                self.set_table(base_tables)

    def set_table(self, args):
        """
        create the sql order to create table
        :param args:
        :return:
        """
        for table_name, args in args.items():
            sql = f'CREATE TABLE IF NOT EXISTS {table_name} ('
            for counter, arg in enumerate(args):
                sql += arg
                if counter < len(args) - 1:
                    sql += ', '
            sql += ');'
            self.create_tables(sql)
        

    def create_tables(self, sql):
        """
        Create the table using the sql order
        :param sql:
        :return:
        """
        # constuire les relations entre les tables
        self.sql_db.create_table(sql)

if __name__ == '__main__': # importされたとき、__name__の値はそのファイル名。__main__になるのは、実行ファイルのとき。
    # TODO Add argparse and logging
    database = DB('db/database.db')
    db = DbBuilder(database)
# if __name__ == '__main__':は毎回一番下。
# 

    ''' Populate base table '''

