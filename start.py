# -*- coding: utf-8 -*-
'''
@Time : 2022/9/14 10:16
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : start.py
'''
__author__ = "梦无矶小仔"

from utils import index
import shutil

def start():
    deleteUtilslog()
    index.main()

def deleteUtilslog():
    try:
        shutil.rmtree("utils/log")
    except:
        pass

# 从根目录启动，确保相对路径调用正常
if __name__ == '__main__':
    # os.popen('adb start-server') #针对android设备
    start()
