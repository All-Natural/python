# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 09:21:06 2021

@author: dyy
"""
import sqlite3
from matplotlib import pyplot as plt,font_manager
#设置支持中文字体的显示
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
font=font_manager.FontProperties(fname="C:/Windows/Fonts/simhei.ttf",size=20)
dbname='films.db'

def getStarImg(fno):
    """代码整合,获取所有的饼图"""
    allCommImg=createAllImg(fno)
    top100Img=createTop100Img(fno)

    return allCommImg,top100Img


def createTop100Img(fno:str):
    """生成支持率Top-100的星级分布图"""
    print(f"fno={fno}")
    sql="""
        select  x.star,count(*)
          from  (
        			select a.fno,a.content,a.star,a.votes
        				from comments as a
        			 where a.content is not null
        				 and a.content!=''
        				 and fno=?
        			 order by a.votes desc
        			 limit 100
        	) x
         group by x.star
         order by x.star
    """
    with sqlite3.connect(dbname)as conn:
        cursor=conn.cursor()
        cursor.execute(sql,[fno])
        rows=cursor.fetchall()
    top100List=[0,0,0,0,0]

    """
    rows=[(1,30),    ---0
          (2,40),    ---1
          (3,140),   ---2
          (4,567),   ---3
          (5,45)     ---4
        ]
    """
    for row in rows:
        top100List[int(row[0])-1]=row[1]

    print(f"top100List={top100List}")
    imgName=f"{fno}_pic_Top100"
    #返回生成饼图名称
    return createPicImg('Top-100星图',top100List,imgName)
    # return ""

def createAllImg(fno:str):
    """生成全部影评的星级分布图"""
    sql="""
     select a.star,count(*)
       from comments a
      where a.fno=?
      group by a.star
      order by a.star
    """
    with sqlite3.connect(dbname)as conn:
        cursor=conn.cursor()
        cursor.execute(sql,[fno])
        rows=cursor.fetchall()
    allCommList=[0]*5
    for row in rows:
        allCommList[int(row[0])-1]=row[1]


    #返回生成饼图名称
    imgName=f"{fno}_pic_all"
    return createPicImg('全部影评星图',allCommList,imgName)
    # return ""

def createPicImg(title:str,data:list,imgName:str):
    """生成饼图"""
    plt.figure(figsize=(6,9)) #调节图形大小
    plt.title(title,fontproperties=font)     #设置图形的字体
    labs=['1star','2star','3star','4star','5star']  #星级各扇区标题
    cols=['#9467bd','#1f77b4','#ff7f0e','#2ca02c','#d62728']  #星级各扇区的演示
    exps= [0.03]*5 #饼图扇区间隙，值越大分割出的间隙越大
    patches,l_text,p_text =plt.pie(data,                 #扇区数据
                                   explode=exps,      #扇区间隙
                                   labels=labs,        #扇区标题
                                   colors=cols,        #各扇区颜色
                                   autopct = '%3.2f%%',  #数值保留固定小数位
                                   shadow = True,        #是否有阴影设置
                                   startangle =15,       #逆时针起始角度设置
                                   pctdistance = 0.75)   #数值距圆心半径倍数距离
    # 内外字体的字号
    for t in l_text:t.set_size(16)
    for t in p_text:t.set_size(12)

    imgName=f'resource/tem/{imgName}.jpg'
    plt.axis('equal')
    plt.legend()
    # bbox_inches='tight' 紧凑型 缩小边缘留白,pad_inches=1 设置留白尺寸
    # plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    # plt.margins(0, 0)
    # plt.savefig(imgName,dpi=200)
    plt.savefig(imgName,dpi=120,bbox_inches='tight',pad_inches=0.01)
    plt.show()
    return imgName


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