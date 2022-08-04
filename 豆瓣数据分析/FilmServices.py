# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 10:16:49 2021

@author: dyy
"""

import sqlite3

dbname='films.db'


def deleteById(fid:int):
    """
       单一实例删除
    """
    sql="delete from film where fid=?"
    with sqlite3.connect(dbname) as conn:
        tag=0
        try:
            conn.execute(sql,[fid])
            conn.commit()
            tag=1
        except Exception as ex:
            conn.rollback()
            print(ex)
    return tag

def addFilm(fno:str,fname:str):
    """添加影片"""
    #定义SQL语句
    sql="""
       insert into film(fno,fname) values(?,?)
    """
    #执行SQL
    with sqlite3.connect(dbname) as conn:
        tag=0
        try:
           conn.execute(sql,[fno,fname])
           conn.commit()
           tag=1
        except Exception as ex:
           conn.rollback()
           print(ex)
    return tag



def queryFilm():
    """查询影片"""
    sql="""
       select fid,fno,fname
         from film
    """
    with sqlite3.connect(dbname) as conn:
        cursor=conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()






