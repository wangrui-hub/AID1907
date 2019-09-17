#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Author: rui.wang
Email: m13717529667@163.com
Tel: 13717529667
Version: v1.0
date: 2019/9/16 下午3:29
"""

import pymysql


def main():
    db = pymysql.connect(host="192.168.12.10",
                         port=33066,
                         user="ruiwang",
                         passwd= "123456",
                         database='stu',
                         charset="utf8")
    cur = db.cursor()
    # name = input("name:")
    # age = input("age:")
    # score = input("score:")
    try:
        # sql = "insert into class_1 (name,age,score) values('%s','%s','%s')" % (name,age,score)
        # sql = "insert into class_1 (name,age,score) values (%s,%s,%s)"
        sql = "update class_1 set score=91 where name = 'abby'"
        # cur.execute(sql,(name,age,score))
        cur.execute(sql)
        sql = "delete from class_1 where name = 'Jack'"
        cur.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    cur.close()
    db.close()


if __name__ == '__main__':
    main()

