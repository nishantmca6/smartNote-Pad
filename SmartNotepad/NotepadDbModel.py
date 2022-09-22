import os
import sqlite3
from sqlite3.dbapi2 import DatabaseError
import traceback
from typing import Counter


class Db_Model:
    def __init__(self):
        self.file_dict = {}
        self.db_status = True
        self.conn = None
        self.cur = None
        try:
            self.conn = sqlite3.connect("test.db")
            print('connected successfully')
            self.cur = self.conn.cursor()
        except DatabaseError:
            self.db_status = False
            print("DB Error : ", traceback.format_exc())

    def get_db_status(self):
        return self.db_status

    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()

    def add_file(self, file_name, file_path, file_owner, file_pwd):
        self.file_dict[file_name] = (file_path, file_owner, file_pwd)
        print("file added:", self.file_dict[file_name])

    def get_file_path(self, file_name):
        return self.file_dict[file_name][0]

    def add_file_to_db(self, file_name, file_path, file_owner, file_pwd):
        self.cur.execute("select max(file_id) from mysecurefiles")
        last_file_id = 1
        if last_file_id is not None:
            next_file_id = last_file_id+1
        self.cur.execute(
            "insert into mysecurefiles values(:1,:2,:3,:4,:5)", (next_file_id, file_name, file_path, file_owner, file_pwd))
        self.conn.commit()
        return "file successfully added to your Databaase"

    def load_files_from_db(self):
        self.cur.execute(
            "select file_name,file_path,file_owner,file_pwd from mysecurefiles")
        file_present = False
        for file_name, file_path, file_owner, file_pwd in self.cur:
            self.file_dict[file_name] = (file_path, file_owner, file_pwd)
            file_present = True
        if file_present is True:
            return "file populated from Database"
        else:
            return "No files present in your Databse"

    def remove_file_from_db(self, file_name):
        self.cur.execute(
            "delete from mysecurefiles where file_name=:1", (file_name,))
        Count = self.cur.rowcount
        if Count == 0:
            return "file not present in your Database"
        else:
            self.file_dict.pop(file_name)
            self.conn.commit()
            return "file deleted from your Database"

    def is_secure_file(self, file_name):
        return file_name in self.file_dict

    def get_file_pwd(self, file_name):
        print(file_name)
        return self.file_dict[file_name][1]

    def get_file_count(self):
        return len(self.file_dict)

    def get_file_owner(self, file_name):
        return self.file_dict[file_name][2]

    # dict structure file_name:file_path,file_pwd,file_owner
