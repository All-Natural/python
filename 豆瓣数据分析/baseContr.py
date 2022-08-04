# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:24:11 2021

@author: dyy
"""
import tkinter as tk
from tkinter import ttk
import sqlite3

dbname='films.db'

def newWindow(title:str='新窗口',up:int=5,win_width:int=160,win_height:int=90,
              offset:int=40,resize:bool=False):
    """创建窗体对象"""
    #创建窗体对象
    win=tk.Tk()
    #设置标题
    win.title(title)
    #窗口的高度和宽度
    w=win_width*up
    h=win_height*up
    #获取屏幕的高度和宽度
    screenw=win.winfo_screenwidth()
    screenh=win.winfo_screenheight()
    #设置窗口的起始坐标
    x=(screenw-w)/2-offset
    y=(screenh-h)/2-offset
    #重构窗口的几何属性--让以上属性设置生效
    win.geometry("%dx%d+%d+%d" % (w,h,x,y))
    #设置窗口是否可以放大
    win.resizable(resize,resize)
    #返回窗口
    return win

def newLabel(root,title,fontSize=12):
    """创建标签对象"""
    tk.Label(root,text=title,font=('微软雅黑',fontSize)).pack(side='left')

def newEntry(root,title):
    """创建带有标签的单行文本框对象"""
    tk.Label(root,text=title).pack(side='left')
    value=tk.StringVar() #文本框的数据容器
    tk.Entry(root,textvariable=value).pack(side='left')
    return value

def newHr(root,color='#50afe5',w=160):
    """可以自定义长度的线段"""
    tk.Frame(root,bg=color,width=w,height=2).pack()

def newEmptyRow(root):
    """显示空行,行的分割线"""
    tk.Frame(root,height=10).pack()

def newRadio(root,data,title='',defVal='1'):
    """创建单选按钮"""
    tk.Label(root,text=title).pack(side='left')
    #定义单选按钮的数据容器
    value=tk.StringVar()
    value.set(defVal)
    #循环data对象,创建单选按钮组
    for tup in data:
        tk.Radiobutton(root,value=tup[1],text=tup[0],variable=value).pack(side='left')
    return value

def newSelect(root,labels:tuple,title:str='',defVal:int=0):
    """创建静态下拉列表"""
    tk.Label(root,text=title).pack(side='left')
    #创建下拉列表
    com=ttk.Combobox(root,state='readonly')
    com.pack(side='left')
    #挂接显示的文本
    com['values']=labels
    #指定默认值
    com.current(defVal)
    return com


def newSelectReadFile(root,fielName:str,title:str='',defVal:int=0):
    """
        Parameters
        ----------
            root :  tk.Frame
            .   容器对象
            fielName : str
                读取的文件名称.
            title : str, optional
                下拉列表的标题.
            defVal : int, optional
                默认被选中的项目的索引.
        Returns
        -------
           下拉列表对象,下拉列表对象的编码元组.

    """
    #控件名称
    tk.Label(root,text=title).pack(side='left')
    #定义select控件的 label和code列表
    labels=[]
    codes=[]
    #读取文件,初始化label和code列表
    with open(fielName,'r',encoding='utf-8') as fr:
        #遍历文件
        for row in fr:
            #拆分当前行数据
            option=row.split(":")
            #向codes和labels写入数据
            codes.append(option[0])
            labels.append(option[1])

    #创建下拉列表控件
    com=ttk.Combobox(root,state='readonly')
    com.pack(side=tk.LEFT)
    #挂接label
    com['values']=labels
    #指定默认值
    com.current(defVal)
    #处理返回值
    return com,codes


def getSelect(root,fname:str,title:str='',defVal:int=0):
    """读取数据库,生成下拉列表"""
    #控件名称
    tk.Label(root,text=title).pack(side='left')
    #为select控件定义code和label列表
    labels=[]
    codes=[]
    #定义SQL语句
    sql="select fcode,fvalue from syscode where isv=? and fname=?"
    #连接数据库
    with sqlite3.connect(dbname) as conn:
        #获取游标
        cursor=conn.cursor()
        #基于游标执行SQL语句
        cursor.execute(sql,['1',fname])
        #读取查询结果
        rows=cursor.fetchall()
    #解析查询结果,填充select的code和label列表
    for ins in rows:
        codes.append(ins[0])
        labels.append(ins[1])

    #创建下拉列表控件
    com=ttk.Combobox(root,state='readonly')
    com.pack(side=tk.LEFT)
    #挂接label
    com['values']=labels
    #指定默认值
    com.current(defVal)
    #处理返回值
    return com,codes

def newText(root:tk.Frame,title:str,w:int=45,h:int=7):
    """创建带有滚动条的大文本域"""
     #控件名称
    tk.Label(root,text=title).pack(side='left')

    """大文本域"""
    #创建文本框容器对象
    rowtext=tk.Frame(root)
    # 创建文本框text，设置宽度w，文本显示的行数设置为h行
    text=tk.Text(rowtext,width=w,font=('微软雅黑',11),height=h)
    text.grid(row=4,column=1,sticky=tk.S + tk.W + tk.E + tk.N)
    # 创建滚动条
    scroll = tk.Scrollbar(rowtext,orient="vertical",command=text.yview)
    # 将滚动条填充
    text.config(yscrollcommand = scroll.set)
    # 将滚动条与文本框关联
    scroll['command']=text.yview
    scroll.grid(row=4,column=2, sticky=tk.S + tk.W + tk.E + tk.N)
    rowtext.pack(side='left')
    return text


def showDataTree(tree,rows):
    #---删除原数据
    items = tree.get_children()  #获取tree对象的数据集合
    [tree.delete(item) for item in items]
    #显示查询结果
    colIndex=0
    for row in rows:
        rowList=list(row)[1:] #将元组转换为list,并踢掉第一列的did
        rowList.insert(0,colIndex+1) #为当前行数据增加序号
        # row_tup=tuple(rowList)
        #给当前行添加一个无标题列,tree内部将该列标记为text,值为该条数据的主键
        tree.insert("", colIndex, text=row[0], values=rowList)
        colIndex=colIndex+1

def reloadTreeView(tree):
    """重新加载TreeView的数据"""
    #5.重新整理TreeView的数据,对数据重新编号,避免跳行
    #5.1.获取TreeView的数据集对象
    items=list(tree.get_children())
    if items:
        print(f"items={items},focus={tree.focus()}")
        #5.2.从items中,删除选中行的treeView标识
        items.remove(tree.focus())
        #5.3.定义列表对象,装载整理后的原始数据
        rows=[]
        #5.4.遍历items中的每个treeView标识
        for item_id in items:
            #5.5.获取该标识对应的行对象
            rowItem=tree.item(item_id)
            #5.6.获取当前行的数据列表
            rowList=rowItem['values']
            #5.7.将当前行数据列表的序号,替换为主键
            rowList[0]=rowItem['text']
            #5.8.将当前行数据,放入rows
            rows.append(rowList)

        #是否存在可以显示的数据
        if rows:
            #显示数据
            showDataTree(tree, rows)


def newTree(root:tk.Frame,titleTuple:tuple,services=None):
    """创建数据窗口对象"""
    cols=[title[0] for title in titleTuple]        #创建表格的标题列表
    ybar=tk.Scrollbar(root,orient='vertical')#竖直滚动条
    tree=tk.ttk.Treeview(root,
                         show='headings', #隐藏text空列
                         height=16,
                         columns=cols,
                         yscrollcommand=ybar.set)

    #表头设置--无需变更
    for col in cols:
         tree.heading(col,text=col,command=lambda col=col:tk.tree_sort_column(tree,col,False))#行标题
    #设置各列的宽度--根据需要调整
    for title in titleTuple:
        tree.column(title[0],width=title[1],anchor=title[2])

    ybar['command']=tree.yview
    tree.grid(row=0,column=0)#grid方案
    ybar.grid(row=0,column=1,sticky='ns')


    #为treeview绑定双击事件
    def delrow(event):  #双击事件的脚本程序
           if services:
              #1.获取treeView中当前选中的行对象
              currItem=tree.item(tree.focus())  #tree.focus()选中行在tree中的id
              #2.获取选中行数据,对应的数据库主键
              dataId=currItem.get('text')
              #3.执行物理删除
              msg='删除成功' if services.deleteById(dataId) else '删除失败!'
              #4.提示消息
              tk.messagebox.showinfo('提示',msg)
              #5.重新加载treeView的数据
              reloadTreeView(tree)

    tree.bind('<Double-1>',delrow)



    return tree


if __name__ == '__main__':
    mainwin=newWindow('员工管理',7)
    #显示窗口
    mainwin.mainloop()








