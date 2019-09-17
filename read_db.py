#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Author: rui.wang
Email: m13717529667@163.com
Tel: 13717529667
Version: v1.0
date: 2019/9/16 下午2:40
"""

import pymysql


def main():
    db = pymysql.connect(host="192.168.12.10",
                         port=33066,
                         user='ruiwang',
                         passwd='123456',
                         database='stu',
                         charset='utf8')
    cur = db.cursor()
    sql = "select name,hobby from interest where hobby = 'draw';"
    cur.execute(sql)
    # for i in cur:
    #     print(i)
    # all_row = cur.fetchall()
    # print(all_row)
    # many_row = cur.fetchmany(1)
    # print(many_row)
    one_row = cur.fetchone()
    print(one_row)
    cur.close()
    db.close()


if __name__ == '__main__':
    main()

