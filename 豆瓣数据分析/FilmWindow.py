# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:38:53 2021

@author: dyy
"""

import baseContr as bc
import MainWindow as mw
import tkinter as tk
import FilmServices as fs
import MessageBoxWindow as msgbox


def openWindow():
    win=bc.newWindow("影片管理",6)

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
    #-------------------------------------------------------------------------

    cols=('序号','影片编号','影片名称','')  #创建表格的标题列表
    ybar=tk.Scrollbar(row1,orient='vertical')#竖直滚动条
    tree=tk.ttk.Treeview(row1,
                         show='headings', #隐藏text空列
                         height=16,
                         columns=cols,
                         yscrollcommand=ybar.set)

    #表头设置--无需变更
    for col in cols:
         tree.heading(col,text=col,command=lambda col=col:tk.tree_sort_column(tree,col,False))#行标题
    #设置各列的宽度--根据需要调整
    tree.column('序号',width=60,anchor='center')
    tree.column('影片编号',width=200,anchor='center')
    tree.column('影片名称',width=200,anchor='center')
    tree.column('',width=40,anchor='center')


    ybar['command']=tree.yview
    tree.grid(row=0,column=0)#grid方案
    ybar.grid(row=0,column=1,sticky='ns')

    #为treeview绑定双击事件
    def delrow(event):  #双击事件的脚本程序
            curItem = tree.focus() #选中行在tree中的id
            #选中行数据的text属性--该属性在放置数据时候,填充的是主键值
            dataId=tree.item(curItem).get("text")
            print(f"选中行的id是{dataId}")

    tree.bind('<Double-1>',delrow)


    #-------------------------------------------------------------------------
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












