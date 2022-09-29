# -*- coding: utf-8 -*-
'''
@Time : 2022/9/19 17:26
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : ParameterizedTestCase.py
'''
__author__ = "梦无矶小仔"

import unittest

class ParameterizedTestCase(unittest.TestCase):
    """ 继承unittest.TestCase类，ParameterizedTestCase类可以进行参数化
        使用时直接继承ParameterizedTestCase类
        注意：methodName不要赋值，否则test不生效
    """
    def __init__(self, methodName, device_id=None):
        super(ParameterizedTestCase, self).__init__(methodName)
        self.device_id = device_id

    @staticmethod
    def parameterize(testcase_class, device_id=None):
        """ 创建一个套件，其中包含给定的测试类,参数可以自己定义单个或多个
        :return 返回测试套件
        :device_id 表示传入的参数，可以自定义，需要注意的是，在init中需要同步更新
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, device_id=device_id))
        return suite

