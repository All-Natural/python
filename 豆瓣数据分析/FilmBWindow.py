# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:38:53 2021

@author: dyy
"""

import baseContr as bc
import MainWindow as mw
import tkinter as tk
import FilmServices as fs


def openWindow():
    win=bc.newWindow("影片管理----数据窗口封装测试",4,win_height=120)

    initContr(win)

    def closeThis():
        # #销毁当前窗口
        win.destroy()
        # #打开主窗口
        mw.openWindow()
    #添加事件拦截方法
    win.protocol("WM_DELETE_WINDOW",closeThis)

    win.mainloop()

def initContr(win:tk.Tk):
    """完成控件挂接"""

    bc.newEmptyRow(win)   #-------------分割线--------------

    #创建标题行
    rowTitle=tk.Frame(win)
    bc.newLabel(rowTitle, "影片管理")
    rowTitle.pack()
    bc.newHr(win)

    bc.newEmptyRow(win)   #-------------分割线--------------
    #添加数据窗口
    row1=tk.Frame(win)
    #-------------------------------------------------------------------------
    titleTuple=(('序号',60,'center'),
                ('影片编号',200,'center'),
                ('影片名称',200,'center'))

    tree=bc.newTree(row1, titleTuple,fs)
    #-------------------------------------------------------------------------
    row1.pack()



    bc.newEmptyRow(win)   #-------------分割线--------------

    #编辑第一行的控件
    row2=tk.Frame(win)
    fno=bc.newEntry(row2, '影片编号:')
    fname=bc.newEntry(row2, '         影片名称:')
    bc.newLabel(row2, "    ")

    def addFilm():
        #添加影片
        msg='添加成功!' if fs.addFilm(fno.get(), fname.get()) else '添加失败'
        #显示执行结果
        tk.messagebox.showinfo("提示",msg)

        #查询影片并显示结果
        bc.showDataTree(tree,fs.queryFilm())

    tk.Button(row2,text='  添加  ',command=addFilm).pack(side='left')
    row2.pack()

    #查询数据,显示结果
    bc.showDataTree(tree,fs.queryFilm())




if __name__ == '__main__':
    openWindow()












