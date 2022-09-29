# -*- coding: utf-8 -*-
'''
@Time : 2022/9/20 14:42
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : TEST_Demo_001.py.py
'''
__author__ = "梦无矶小仔"
import unittest
from common.ParameterizedTestCase import ParameterizedTestCase

class TEST_22222wew(ParameterizedTestCase):
    '第一个测试文件'

    # @unittest.skip
    def test001_startAPP(self):
        '001进入第一个页面'
        print(f"当前运行的设备为：{self.device_id}")
        print('001进入第一个页面')

    # @unittest.skip
    def test002_Authorization(self):
        '''001_进行授权'''
        print('001第二个测试用例')

    def test004_IosAtt(self):
        '''001_ios弹出ATT弹窗，点击"允许跟踪"按钮'''
        print('001_ios弹出ATT弹窗，点击"允许跟踪"按钮')





