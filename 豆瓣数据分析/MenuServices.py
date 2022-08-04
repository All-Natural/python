# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:21:51 2021

@author: dyy
 """

import tkinter as tk
import FilmBWindow as fw
import CommentWindow as cw
import CloudWindow as clw
import DataViewWindow as dw

def initMenu(mainWin:tk.Tk):
    """菜单的全部处理"""
    #创建主菜单
    mainMenu=tk.Menu()

    #数据维护
    dataMenu=tk.Menu(tearoff=0)
    #读取ScriptList的内容,创建数据库中表---判断建表语句文件是否存在,存在则创建,不存在则忽略
    """
      应用python 的os模块,可以解决这个问题
      ScriptList.txt----{
              syscode
              emp
              dept
              kpi
          }
      syscode.sql
      emp.sql
      dept.sql
    """
    def createTable():
        pass
    dataMenu.add_command(label='数据库初始化',command=createTable)

    def filmsManager():
        """
           影片管理
        """
        mainWin.destroy()
        fw.openWindow()

    dataMenu.add_command(label='影片管理',command=filmsManager)
    mainMenu.add_cascade(label='数据维护',menu=dataMenu)


    commentMenu=tk.Menu(tearoff=0)  #影片评论管理
    
    
    def getComm():      #爬取评论
        mainWin.destroy()
        cw.openWindow() 

    def getCloud():    #生成词云
        mainWin.destroy()
        clw.openWindow()
    
    def getData():     #分析影评
        mainWin.destroy()
        dw.openWindow()
        
    commentMenu.add_command(label='短评爬取',command=getComm)
    commentMenu.add_command(label='生成词云',command=getCloud)
    commentMenu.add_command(label='认可度分析',command=getData)
    # commentMenu.add_separator()
    # commentMenu.add_command(label='评论爬取')
    # commentMenu.add_command(label='生成词云')
    # commentMenu.add_command(label='认可度分析')
    mainMenu.add_cascade(label='影评管理',menu=commentMenu)



        
    #系统维护
    sysMenu=tk.Menu(tearoff=0)
    sysMenu.add_command(label='口令维护')
    sysMenu.add_separator() #一条分割线
    def exitMainWindow():
        #销毁主窗口
        mainWin.destroy()

    sysMenu.add_command(label='退出',command=exitMainWindow)
    mainMenu.add_cascade(label='系统维护',menu=sysMenu)





    #将菜单挂接到窗口上
    mainWin.config(menu=mainMenu)