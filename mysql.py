#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Author: rui.wang
Email: m13717529667@163.com
Tel: 13717529667
Version: v1.0
date: 2019/9/16 上午9:03
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
    sql = "insert into interest values (3,'Emma','draw','C',14800,'xxx');"
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()


if __name__ == '__main__':
    main()
