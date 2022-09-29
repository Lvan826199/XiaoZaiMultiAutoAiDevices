# -*- coding: utf-8 -*-
'''
@Time : 2022/9/20 14:42
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : TEST_Demo_002.py.py
'''
__author__ = "梦无矶小仔"
# -*- coding: utf-8 -*-
import datetime
import sys
import threading
import time
import traceback

from tidevice import Device
from airtest.core.ios.ios import IOS, wda
from common.screenshot import iosScreenshot
sys.dont_write_bytecode = True
import unittest
import logging
from common.imageElePath import *
from common.IOSAppOperate import SH_182
from tools.get_devices_log import ios_log
from common.ParameterizedTestCase import ParameterizedTestCase

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
_print = print

# ### 设置airtest的日志输出等级,调试时可以注释或者调为INFO
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)

controlparams = {'control':1} # 用作控制器
class TestDemo_2(ParameterizedTestCase):
    u'''测试用例Demo的集合'''
    @classmethod
    def setUpClass(self):
        u''' 这里放需要在整个测试类之前执行的部分'''
        print("setUpClass，在整个测试类之前执行")

    @classmethod
    def tearDownClass(self):
        u'''这里放需要在整个测试类之后执行的部分'''
        controlparams['control'] = 1

    def setUp(self):
        u'''这里放需要在每条用例前执行的部分'''
        # 前段部分用于初始化连接设备，这个部分的作用就是避免设备多次重新连接，只会连接一次
        if controlparams['control'] == 1 :
            self.ios = IOS("http+usbmux://" + self.device_id)
            self.c = wda.Client("http+usbmux://{udid}".format(udid=self.device_id))
            controlparams['ios'] = self.ios
            controlparams['c'] = self.c
            controlparams['control'] = 2
        # 每次执行用例前，需要从控制参数里面进行取出（但不会进行重新连接）
        self.ios = controlparams['ios']
        self.c = controlparams['c']

    def tearDown(self):
        u'''这里放需要在每条用例后执行的部分'''
        # self.c.close() #防止在线程中使用时端口阻塞


########################## app内操作（可以自行封装，也可以直接在这写）

    @classmethod
    def enter_home_page(cls,device_id):
        # 通过首页图标进行判断
        ...

    @classmethod
    def login(cls,device_id):
        # 通过图片进行相关判断，进行截图等操作，此部分根据自己项目需求写就行
        print(f"{device_id}-设备开始登录的各种操作")
        for i in range(5):
            if exists(facebook_continue):
                iosScreenshot(device_id, '继续按钮存在')
                break

####################################  用例  ####################################

    # @Timeout.timeout(30)
    # @unittest.skip
    def test_01_of_loginAppStore(self):
        u'''登录appstore'''
        print("---------开始进行第一个测试用例----------")
        #每个函数里分别实例poco，否则容易出现pocoserver无限重启的情况
        # ###卸载
        Device(self.device_id).app_uninstall("com.mwjxiaozai.stories") # 填入自己公司app的ios包名
        ###安装
        if self.c.locked():
            self.c.unlock()
        if self.ios.alert_exists():
            alert = self.ios.alert_buttons()
            print("检测：",alert)

        if self.c.alert.exists:
            buttons = self.c.alert.buttons()
            self.c.alert.click(buttons)
            print("弹框关闭")
        self.c.close()
        print("````````````````````````````````")
###########################
        # appstore 账号登录
        SH_182().loginAppStore(self.c, "mwjxiaozai@gmail.com", "mwj123456") # 填入用于app store登录的apple id



    # @unittest.skip
    def test_02_of_checkAcount(self):
        '''检查AppleID'''
        # 沙盒账号登录
        print("-------------------进行第二个测试用例---------------------")
        SH_182().check_acount_ios14(self.c, "mwjxiaozai@gmail.com", "mwj123456") # 填入用于app充值的沙盒账号
        ###################################



    # @unittest.skip
    def test_03_of_CheckDownload(self):
        u'''进入TestFlight进行下载App'''
        print("-------------------进行第三个测试用例---------------------")
        ##使用testflight下载对应的app,填入的是在testFlight显示的app全称
        SH_182().App_download(self.c, name="mwj - xiaozai app name")
        iosScreenshot(self.device_id,'app下载成功')
        print("App 下载完毕！")
        print("测试开始")



    # @unittest.skip
    def test_04_of_CheckEnterApp(self):
        u'''检查进入APP功能'''
        print("-------------------进行第四个测试用例---------------------")
        ##启动
        self.c.app_start("com.mwjxiaozai.stories")
        sleep(10)
        ###判断app是否在运行
        app = self.ios.app_state("com.mwjxiaozai.stories")["value"]
        time.sleep(10)
        if app == 4:
            for i in range(3):
                if self.ios.alert_exists():
                    self.ios.alert_accept()
        if self.c.alert.exists:
            buttons = self.c.alert.buttons()
            self.c.alert.click(buttons)
            print("弹框关闭")
        self.enter_home_page(self.device_id)








