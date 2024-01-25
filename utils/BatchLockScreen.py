# -*- coding: utf-8 -*-
"""
@Time : 2024/1/25 17:56
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : BatchLockScreen.py
"""
__author__ = "梦无矶小仔"

from airtest.core.api import *
from airtest.core.ios.ios import wda
import tidevice

# 获取所有连接设备的信息
device_list = tidevice.Usbmux().device_list()

# 将所有的设备udid加入一个列表里面
device_udid_list = []
for device in device_list:
    device_udid_list.append(device.udid)


### 批量解锁
def unlock_device():
    for device_udid in device_udid_list:
        print(device_udid)
        try:
            dev = connect_device(f"iOS:///http+usbmux://{device_udid}")
            c = wda.Client("http+usbmux://{udid}".format(udid=device_udid))
            # 判断屏幕是否锁定,锁定为True,未锁定为False
            if c.locked():
                # 如果锁定了,则解锁
                try:
                    c.unlock()
                except:
                    pass
                print(f"{device_udid}屏幕已解锁")
            else:
                print((f"{device_udid}屏幕原本就是解锁状态"))
        except:
            print(f"{device_udid},设备WDA服务未启动...")


### 批量锁屏
def lock_device():
    for device_udid in device_udid_list:
        print(device_udid)
        try:
            dev = connect_device(f"iOS:///http+usbmux://{device_udid}")
            c = wda.Client("http+usbmux://{udid}".format(udid=device_udid))
            # 判断屏幕是否锁定,锁定为True,未锁定为False
            if not c.locked():
                # 如果锁定了,则解锁
                try:
                    c.lock()
                except:
                    pass
                print(f"{device_udid}屏幕已锁屏")
            else:
                print((f"{device_udid}屏幕原本就是锁屏状态"))
        except:
            print(f"{device_udid},设备WDA服务未启动...")


if __name__ == '__main__':
    ## 批量解锁
    # unlock_device()
    ## 批量锁屏
    lock_device()
