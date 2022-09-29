# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/18 17:33
@Auth ： 梦无矶小仔
@File ：caseMethod.py
@IDE ：PyCharm
"""
import time
import subprocess


'''
Android通过adb命令进行的操作
'''

def mwj_install_apk(deviceName,apkPath):
    try:
        deviceName = deviceName
        apkPath = apkPath
        subprocess.call(f'adb -s {deviceName} install {apkPath}')
        return True
    except:
        return False


def mwj_uninstall_apk(deviceName,packageName):
    try:
        deviceName = deviceName
        packageName = packageName
        subprocess.call(f'adb -s {deviceName} uninstall {packageName}')  # adb shell dumpsys window | findstr mCurren
        return True
    except:
        return False

def mwj_start_apk(deviceName,packageAndActivity):
    try:
        deviceName = deviceName
        packageAndActivity = packageAndActivity
        subprocess.call(f'adb -s {deviceName} shell am start {packageAndActivity}')
        return True
    except:
        return False
