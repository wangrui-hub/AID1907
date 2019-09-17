#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Author: rui.wang
Email: m13717529667@163.com
Tel: 13717529667
Version: v1.0
date: 2019/9/16 下午4:24
"""

import pymysql


def main():
    db = pymysql.connect(host="192.168.12.10",
                         port=33066,
                         user="ruiwang",
                         passwd= "123456",
                         database='dict',
                         charset="utf8")
    cur = db.cursor()
    f = open("dict.txt","r")
    sql = "insert into words (word,mean) values(%s,%s)"
    for line in f:
        # tmp = re.findall(r'(\S+)\s+(.*)',line)[0]
        # cur.execute(sql,tmp)
        tmp = line.split(" ",1)
        word = tmp[0]
        mean = tmp[1].strip()
        cur.execute(sql,(word,mean))
    f.close()
    try:
        db.commit()
    except:
        db.rollback()

    cur.close()
    db.close()


if __name__ == '__main__':
    main()

