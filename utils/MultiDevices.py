# -*- coding: utf-8 -*-
'''
@Time : 2022/9/14 10:54
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : MultiDevices.py
'''
__author__ = "梦无矶小仔"


import os,inspect
import sys
import threading
import queue
from utils import RunTestCase
from utils.readConfig import *
from airtest.core.api import *
from airtest.core.error import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android.adb import ADB
import  subprocess
from airtest.utils.apkparser import APK

adb = ADB().adb_path

class MultiDevices():
    def __init__(self,mdevice=""):
        # 获取当前文件的上层路径
        self.parentPath = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".")
        # 获取当前项目的根路径
        self.rootPath = os.path.abspath(os.path.dirname(self.parentPath) + os.path.sep + ".")
        self._mdevice = mdevice
        # 处理模拟器端口用的冒号
        if ":" in self._mdevice:
            self._nickName = self._mdevice.split(":")[1]
        else:
            self._nickName = self._mdevice

    # 本方法用于读取实时的设备连接
    def getdevices(self):
        android_list = []
        for devices in os.popen(adb + " devices"):
            if "\t" in devices:
                if devices.find("emulator") < 0:
                    if devices.split("\t")[1] == "device\n":
                        android_list.append(devices.split("\t")[0])
                        print("已添加：安卓设备 - {}".format(devices))
        ios_list = []
        try:
            from tidevice import Usbmux
            ios = Usbmux().device_udid_list()
            for i in ios:
                ios_list.append(i)
                print("已添加：苹果设备 - {}".format(i))
        except:
            print("IOS设备未连接，请重新连接！")
        deviceslist = android_list + ios_list
        return deviceslist

    # 获取当前设备id
    def get_mdevice(self):
        return self._mdevice

    #获取当前设备id的昵称，主要是为了防范模拟器和远程设备带来的冒号问题。windows的文件命名规范里不允许有冒号。
    def get_nickname(self):
        return self._nickName

    #修改当前设备的方法
    def set_mdevice(self,device):
        self._mdevice=device

     #判断给定设备的安卓版本号
    def get_androidversion(self):
        if len(self.get_mdevice())>8:
            return 5
        else:
            command=adb+" -s {} shell getprop ro.build.version.release".format(self.get_mdevice())
            version=os.popen(command).read().split(".")[0]
            version=int(version)
            return version

    # 获取测试用例路径，不填是默认根目录TestCase
    def get_TestCasePath(self):
        testCasePath = os.path.join(self.rootPath, "TestCase")
        return testCasePath

    # 获取针对特定设备的用例列表
    def get_testCaseWhichRun(self,device):
        device = str(device).lower() # 该死的config库使用option提取会变小写
        try:
            testCase = getAllTestCase()[device]
            testCaseList = testCase.split(',')
        except KeyError:
            testCaseList = []
        return testCaseList

    # 获取用例的指定文件夹
    def get_SpCaseFolder(self):
        # 获取TestCase下的文件夹
        TestCasePath = os.path.join(self.rootPath,'TestCase')
        ChildFolderList = []
        for root, dirs, files in os.walk(TestCasePath, topdown=False):
            ChildFolderList.append(root)
        getSpCaseFolderList = getSpCaseFolder()
        if len(getSpCaseFolderList)==1 and  getSpCaseFolderList[0]:
            if getSpCaseFolderList[0] == 'all':
                return TestCasePath
            else:
                for ChildFolder in ChildFolderList:
                    if '\\' in ChildFolder:
                        folderName = ChildFolder.split('\\')[-1].lower()
                    elif '/' in ChildFolder:
                        folderName = ChildFolder.split('/')[-1].lower()
                    else:
                        folderName = "None"
                    if getSpCaseFolderList[0] == folderName:
                        return ChildFolder
                else:
                    print(f"请在TestCase文件夹中添加【{getSpCaseFolderList[0]}】文件夹及用例！")
                    return None

        else:
            print('TestCaseSpFolder中的选项只能有一个为1')
            return None






if __name__ == '__main__':
    cc = MultiDevices()
    print(cc.get_testCaseWhichRun('00008110-000275943eeb801e'))
    print(cc.get_SpCaseFolder())
    # print(cc.rootPath)