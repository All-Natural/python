# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:29:52 2021

@author: dyy
"""

import sqlite3
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘图模块


WC_FONT_PATH = 'C:/Windows/Fonts/simhei.ttf'  #词云字体
dbname='films.db'

def createWordImage(fno:str,keyCount:int=30):
    """
      生成该影片的词云图片,
      返回图片的存储位置及名称
    """
    print(keyCount,type(keyCount))

    """生成词云"""
    #获取该影片的短评
    comms=getCommentForFno(fno)

    #结巴切词--词语提取cut_all=True 全模式 cut_all=False 精准模式(默认)
    wordList=jieba.cut(comms,cut_all=False)
    words=" ".join(wordList) #将提取的词语连接成字符串,词语间以空格间隔

    with open('test.txt','w',encoding='utf-8') as fr:
        fr.write(words)


    #获取违禁词汇列表
    stopWordsList=getStopWordsList()
    #实例化词云对象
    cloud = WordCloud(background_color="white",
               scale=4,
               max_words=keyCount,       #限定词云中单词的个数
               width=800,height=450,
               max_font_size=65,
               random_state=42,
               stopwords=stopWordsList,   #违禁词汇列表
               font_path=WC_FONT_PATH)
    # 生成词云,词云对象将应用违禁词汇列表,自动对words清洗
    cloud.generate(words)
    #生成词云图片
    cloudImgName=f"resource\\tem\\{fno}.jpg"
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(cloudImgName,dpi=500)
    plt.clf()
    return cloudImgName


def getStopWordsList():
    """生成违禁词汇列表"""
    with open(r'resource\stopWordsList.txt','r',encoding='utf-8') as fr:
        return fr.read().splitlines()


def getCommentForFno(fno):
    """按编号获取短评字符串"""
    sql="""
            select group_concat(content)
              from comments
             where fno=?
    """
    with sqlite3.connect(dbname) as conn:
        cursor=conn.cursor()
        cursor.execute(sql,[fno])
    return cursor.fetchone()[0]

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