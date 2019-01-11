# _*_ coding: utf-8 _*_
# description: initlize the database and save the fingercode

import sqlite3
import os


def initlize_db(db_name):

    # if have existed
    if os.path.isfile(db_name):
        print "this database has existd......"
        return

    # initlizing the database
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    # create tables
    tables_sql = 'create table fingercode (id int, image_name text, angle0 text, angle1 text, angle2 text, angle3 text,' \
                 'angle4 text, angle5 text, angle6 text, angle7 text)'

    print "initlizing the database now ......"
    c.execute(tables_sql)
    conn.commit()
    conn.close()
    print "initlizing the database is ok....."


# save the fingercode
def save_fingercode(db_name, result):

    print "start saving the result...."
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    sql = "INSERT INTO fingercode VALUES (?,?,?,?,?,?,?,?,?,?)"
    c.execute(sql, result)
    print "execute....."
    conn.commit()
    print "commit...."
    conn.close()
    print "close..."


# get the fingercode
def get_fingercode(db_name):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    sql = "select * from fingercode where id=?"
    c.execute(sql, '1')
    result = c.fetchone()
    conn.close()
    return result


# get all data
def get_all(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    print "start getting all..."
    c.execute('select * from fingercode')
    result = c.fetchall()
    conn.close()
    print "close...."
    return result
