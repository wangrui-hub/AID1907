#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Author: rui.wang
Email: m13717529667@163.com
Tel: 13717529667
Version: v1.0
date: 2019/9/16 下午5:27
"""
import sys

import pymysql


class User(object):
    def __init__(self, user, passwd, database, charset="utf8", host="127.0.0.1", port=3306, ):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.login_database()

    def login_database(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)
        self.cur = self.db.cursor()

    def login(self, username, passwd):
        sql = "select passwd from users where user='%s'"
        try:
            self.cur.execute(sql, username)
        except Exception:
            sys.exit("no such name")
        data = self.cur.fetchone()
        if data[0] == passwd:
            print("login sucessful")
        else:
            print("passwd is wrong")

    def regiester(self, name, passwd):
        sql = "select username from user where username='%s'"
        self.cur.execute(sql,[name])
        data = self.cur.fetchone()
        if data:
                return False
        sql = "insert into users(username,passwd) values(%s,%s)"
        try:
            self.cur.execute(sql,(name, passwd))
            self.db.commit()
            return True
        except:
            self.db.rollback()


def main():
    user = User("ruiwang", "123456", "logins", host="192.168.12.10", port=33066)


if __name__ == '__main__':
    main()
