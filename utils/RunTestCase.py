# -*- coding: utf-8 -*-
'''
@Time : 2022/9/14 10:54
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : RunTestCase.py
'''
__author__ = "梦无矶小仔"


import unittest
from airtest.core.api import *
from TestCase import *
from unittestreport import TestRunner
import unittestreport
from datetime import datetime
from common.ParameterizedTestCase import ParameterizedTestCase

_print = print
def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)

#运行Testcase
def RunTestCase(MD,start):
    ### 使用者可以根据自己的需求，将unittest框架更改为pytest框架，这个报告都兼容
    device_id=MD.get_mdevice()
    print("进入{}的RunTestCase".format(device_id))
    # 获取路径
    TestCasePath = MD.get_TestCasePath()
    if not os.path.exists(TestCasePath):
        print("测试用例需放到‘TestCase’文件目录下")
    reportpath = os.path.join(os.getcwd(), "Reports")
    #读取ini文件，获得期望测试的用例(这里只做了一个文件，可以使用多个，以后再加)
    testCaseList = MD.get_testCaseWhichRun(device_id)
    print("{}的待测用例为：{}".format(MD.get_mdevice(),testCaseList))
    SpCaseFolderPath = MD.get_SpCaseFolder()
    if '\\' in  str(SpCaseFolderPath):
        SpCaseFolderName = str(SpCaseFolderPath).split('\\')[-1]
    else:
        SpCaseFolderName = str(SpCaseFolderPath).split('/')[-1]


    # 没有测试用例，直接不出报告
    # 未对All选项的测试集进行适配，只适配了单个文件夹下的，如果不需要传参数进入TestCase，则可以不用适配（有生之年我可能会适配一下）
    if testCaseList:
        suite = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(start_dir=SpCaseFolderPath,pattern='TEST*.py')
        for test_suite in discover:
            try:
                test_suite_py_name = str(test_suite._tests[0]).split('tests=[<')[1].split('.')[0].strip()
                test_class_name = str(test_suite._tests[0]).split('tests=[<')[1].split('.')[1].split(' ')[0].strip()
            except:
                try:
                    test_suite_py_name = str(test_suite._tests[1]).split('tests=[<')[1].split('.')[0].strip()
                    test_class_name = str(test_suite._tests[1]).split('tests=[<')[1].split('.')[1].split(' ')[0].strip()
                except: # 过滤掉没有测试用例的case
                    continue
            if test_suite_py_name in testCaseList:
                exec(f'from TestCase.{SpCaseFolderName}.{test_suite_py_name} import {test_class_name}')
                x = locals()
                suite.addTest(ParameterizedTestCase.parameterize(eval(x['test_class_name']),device_id=device_id))

        # 对设备进行重命名,生成的测试报告以这个名字为标题，默认为设备ID
        if MD.get_nickname() == '00008101-001859DE1E38001E':  # SH-SJ-0123
            reportName = 'SH-SJ-0123'
        elif MD.get_nickname() == '00008030-001E19021A42802E':  #  #SH-SJ-0186
            reportName = 'SH-SJ-0186'
        else:
            reportName = MD.get_nickname()

        nowtime = time.strftime("%Y-%m-%d_%H-%M-%S", start)
        runner = TestRunner(suite,
                            title=f'{reportName}测试报告',
                            filename=f"{nowtime}_{reportName}.html",
                            report_dir=reportpath,
                            templates=2,
                            tester='梦无矶小仔')
        runner.run()







