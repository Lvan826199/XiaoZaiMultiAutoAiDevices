# -*- coding: utf-8 -*-
'''
@Time : 2022/9/14 10:18
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : start_ios_devices.py
'''
__author__ = "梦无矶小仔"

'''
文件说明:
开启ios设备的WebDriverAgent服务，需自行配置好相关环境，包名需更改为你在xcode中打包的包名
详细教程参考我的博客:https://blog.csdn.net/qq_46158060/article/details/125977466
'''
import os
def get_ios_devices():
    print("===============================================================")
    print("========= 识别扫描连接IOS设备，开启tidevice终端=================")
    print("===============================================================")
    s = os.popen("tidevice list")
    s = s.buffer.readlines()
    ios_list = []
    for ios in s[1:]:
        if len(ios.split()) > 1:
            ios = ios.decode('utf-8')
            ios_list.append(ios.split()[0])
            print("苹果设备{}被扫描识别".format(ios.split()[0]))
    print(f'本次共扫描出{len(ios_list)}个苹果设备')
    port = 10
    for devices in ios_list:
        port+=1
        print(devices)
        os.popen( "tidevice --udid "+ str(devices) +" xctest -B com.facebook.WebDriverAgentRunnerxzz.xctrunner -e USB_PORT:81"+ str(port)+'')
        print(f"开启成功：{devices}：81{port}")
    return True

if __name__ == '__main__':
    get_ios_devices()