# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:29:52 2021

@author: dyy
"""


import tkinter as tk
import baseContr as bc
import DataServices as ds
import MainWindow as mw
#操作图片
from PIL import ImageTk
import PIL

def openWindow():
    win=bc.newWindow("影评星级分析",6)

    bc.newEmptyRow(win)
    bc.newEmptyRow(win)  #---------间隔线------------------------

    #标题行
    row1=tk.Frame(win)
    bc.newLabel(row1,'影评星级分析')  #创建标题
    row1.pack()
    bc.newHr(win)
    bc.newEmptyRow(win)  #--------间隔线------------------------

    row3=tk.Frame(win)
    up=0.5
    starName="resource\\pic_all.jpg"
    starBgImg = PIL.Image.open(starName).resize((int(638*up),int(855*up)),PIL.Image.ANTIALIAS)
    starimg=ImageTk.PhotoImage(starBgImg)
    starImgLabel=tk.Label(row3,image=starimg)
    starImgLabel.pack(side='left')

    starTopName="resource\\pic_top100.jpg"
    starTopBgImg = PIL.Image.open(starTopName).resize((int(638*up),int(855*up)),PIL.Image.ANTIALIAS)
    starTopImg=ImageTk.PhotoImage(starTopBgImg)
    starTopImgLabel=tk.Label(row3,image=starTopImg)
    starTopImgLabel.pack(side='left')



    bc.newEmptyRow(win)  #-----间隔线------------------------

    row2=tk.Frame(win)     #第二行控件
    #获取影片名称及编号的列表
    fnoList,fnameList=ds.getFilmList()
    #生成页面显示的影片下拉列表
    filmList=bc.newSelect(row2, fnameList,'影片列表:   ')

    bc.newLabel(row2, "     ")#行内间隔
    def getComm():
        """影评星级分析"""
        fno=fnoList[filmList.current()]
        imgs=ds.getStarImg(fno)
        print(imgs,imgs[0],imgs[1])
        #星级分布图
        newStarName=imgs[0]
        newStarTem=PIL.Image.open(newStarName).resize((int(638*up),int(855*up)),PIL.Image.ANTIALIAS)
        newStarImgTk=ImageTk.PhotoImage(newStarTem)
        starImgLabel.configure(image=newStarImgTk)
        starImgLabel.image = newStarImgTk


        #Top100星级分布图
        newStarTopName=imgs[1]
        newStarTopTem=PIL.Image.open(newStarTopName).resize((int(638*up),int(855*up)),PIL.Image.ANTIALIAS)
        newStarTopImgTk=ImageTk.PhotoImage(newStarTopTem)
        starTopImgLabel.configure(image=newStarTopImgTk)
        starTopImgLabel.image = newStarTopImgTk


    tk.Button(row2,text=' 分析  ',command=getComm).pack()   #创建按钮



    row2.pack()
    bc.newEmptyRow(win)  #-----间隔线------------------------
    row3.pack()

    def closeThis():
        # #销毁当前窗口
        win.destroy()
        # #打开主窗口
        mw.openWindow()
    #添加事件拦截方法
    win.protocol("WM_DELETE_WINDOW",closeThis)
    win.mainloop()


if __name__ == '__main__':
    openWindow()
