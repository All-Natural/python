# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:13:15 2021

@author: dyy
"""

import sqlite3
import random
import time
import requests
import tkinter as tk
import re  #正则表达式

dbname='films.db'

def getFilmComm(fno:str,fname:str,infoBox:tk.Text):
    """获取影片短评"""

    #定义类别字典
    typeDict={'h':'好评','m':'一般','l':'差评'}
    #创建于目标网址的会话对象
    session=requests.Session()
    #定义请求头
    headers = {'user-agent': 'Mozilla/5.0'}
    #循环短评类别
    for commType in "hml":
        #设置当前类别的页码
        pageNumber=1
        #当前类别爬取结束标记
        typeEnd=False
        while not typeEnd:
            #计算当前页码的起始行
            startRow=(pageNumber-1)*20
            #拼接本页短评的url
            url=f"https://movie.douban.com/subject/{fno}/comments?percent_type={commType}&start={startRow}&limit=20&status=P&sort=new_score"
            #向目标地址提交请求
            try:

               result=session.get(url,headers=headers)
               result.raise_for_status()   #抛出异常

               msg=f"爬取影片{fname},的第{pageNumber}页{typeDict[commType]} 类型的短评成功----\n"
               infoBox.insert('end',msg)
               infoBox.yview_moveto(1)
               infoBox.update()

               #解析当前页码的短评
               commList=parseHtml(fno,result.text)
               #存储当前页码的数据
               saveComment(commList)

               pageNumber+=1
            except Exception:
               #设置当前类别结束标记
               typeEnd=True
            #模拟正常工作,线程等待随机时间
            time.sleep(random.random()*3)
    msg=f"========影片{fname}的所有类型的短评爬取结束========\n"
    infoBox.insert('end',msg)
    infoBox.yview_moveto(1)
    infoBox.update()

def saveComment(commList:list):
    """短评保存"""
    sql="""
       insert into comments(fno,content,star,votes)
                     values(?,?,?,?)
    """
    with sqlite3.connect(dbname) as conn:
        tag=0
        try:
            conn.executemany(sql,commList)
            conn.commit()
            tag=1
        except Exception as ex:
            conn.rollback()
            print(ex)
    return tag


def parseHtml(fno:str,text:str):
    """解析网页源代码"""

    htmlComm=[]  #当前页面的所有短评

    #制定数据筛选规则----正则表达式筛选规则
    pattern = re.compile(r'<div class="comment">.*?</div>',re.S)  #制定规则
    #获取迭代器
    commentIters = re.finditer(pattern,text)     #执行规则,批量提取
    #遍历迭代器
    for ci in commentIters:
        print("---------------------------------------")
        commText=ci.group()  #一条短评

        #提取评论的内容
        commList=re.findall('<span class="short">(.*)</span>',commText)
        #判断短评内容是否存在
        if len(commList):
            #获取星级
            starList=re.findall('<span class="allstar(.*?). rating" title=".*"></span>',commText)  #数据精准提取
            print(starList)
            star=starList[0] if len(starList)>0 else 0
            # print(f"星级:{star}\n")

            #提取该短评的认可人数
            votesList=re.findall('<span class="votes vote-count">(.*)</span>',commText)
            print(f"votesList={votesList}")
            votes=votesList[0] if len(votesList)>0 else 0
            # print(votes)

            #将本条评论的解析内容,加入返回值列表
            htmlComm.append((fno,commList[0],star,votes))

    return htmlComm



def getFilmList():
    """获取影片列表"""
    # 定义影片编号及名称列表
    fnoList=[]
    fnameList=[]

    sql="select distinct fno,fname from film order by fname"
    with sqlite3.connect(dbname) as conn:
        cursor=conn.cursor()
        cursor.execute(sql)
        #解析数据,生成列表
        for row in cursor:
              fnoList.append(row[0])
              fnameList.append(row[1])


    return fnoList,fnameList


if __name__ == '__main__':
    # with open('html.txt','r',encoding='utf-8') as fr:
    #     text=fr.read()
    # commList=parseHtml('10001',text)
    # print(commList)

    f1,f2=getFilmList()
    print(f1,'\n',f2)



