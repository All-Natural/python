# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:20:11 2021

@authordyy
"""
import tkinter as tk
import baseContr as bc
import MenuServices as ms
from PIL import ImageTk
import PIL


def openWindow():
    win=bc.newWindow("豆瓣影评分析",7)
    #为主窗口挂接菜单
    ms.initMenu(win)
    # bc.newEmptyRow(win)  #-----间隔线------------------------    
    # bc.newEmptyRow(win)  #-----间隔线------------------------    
    row1=tk.Frame(win)
    sourceImgPath=r'resource\audience.jpg'   #原始图片的存储位置
    #按照指定大小及质量,生成背景图片
    bgImg = PIL.Image.open(sourceImgPath).resize((int(1280),int(850)),PIL.Image.ANTIALIAS)
     #生成可以在label标签中显示的图片对象
    labelImage=ImageTk.PhotoImage(bgImg)
    #创建标签对象,显示图片
    imgLabel=tk.Label(row1,image=labelImage)
    imgLabel.pack(side='left')
    row1.pack()


    win.mainloop()



 
if __name__ == '__main__':
  openWindow()