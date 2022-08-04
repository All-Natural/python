# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:29:52 2021

@author: dyy
"""


import tkinter as tk
import baseContr as bc
import CloudServices as cs
import MainWindow as mw
#操作图片
from PIL import ImageTk
import PIL

def openWindow():
    win=bc.newWindow("词云获取",6)

    bc.newEmptyRow(win)
    bc.newEmptyRow(win)  #---------间隔线------------------------

    #标题行
    row1=tk.Frame(win)
    bc.newLabel(row1,'词云生成')  #创建标题
    row1.pack()
    bc.newHr(win)
    bc.newEmptyRow(win)  #--------间隔线------------------------

    row3=tk.Frame(win)
    sourceImgPath=r'resource\R-C.jpg'   #原始图片的存储位置
    #按照指定大小及质量,生成背景图片
    bgImg = PIL.Image.open(sourceImgPath).resize((int(800),int(450)),PIL.Image.ANTIALIAS)
     #生成可以在label标签中显示的图片对象
    labelImage=ImageTk.PhotoImage(bgImg)
    #创建标签对象,显示图片
    imgLabel=tk.Label(row3,image=labelImage)
    imgLabel.pack(side='left')


    bc.newEmptyRow(win)  #-----间隔线------------------------

    row2=tk.Frame(win)     #第二行控件
    #获取影片名称及编号的列表
    fnoList,fnameList=cs.getFilmList()
    #生成页面显示的影片下拉列表
    filmList=bc.newSelect(row2, fnameList,'影片列表:   ')
    bc.newLabel(row2, "     ")#行内间隔
    #关键词个数
    keyCount=bc.newSelect(row2, (200,150,100,50,30,20,15,10,5,3,1),'关键词个数',defVal=4)

    bc.newLabel(row2, "     ")#行内间隔
    def getComm():
        """生成词云"""
        imgName=cs.createWordImage(fnoList[filmList.current()],int(keyCount.get()))
        # 显示词云图片
        img_temp = PIL.Image.open(imgName).resize((int(3000*0.29),int(2000*0.2)),PIL.Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img_temp)
        imgLabel.configure(image=img_tk)
        #为imgLabel的图片属性赋值
        imgLabel.image = img_tk

    tk.Button(row2,text=' 生成  ',command=getComm).pack()   #创建按钮



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
