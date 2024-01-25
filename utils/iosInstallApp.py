# -*- coding: utf-8 -*-
"""
@Time : 2024/1/25 17:46
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : iosInstallApp.py
"""
__author__ = "梦无矶小仔"

from airtest.core.api import *
from airtest.core.ios.ios import wda

# 填写ios设备的udid,字典格式，可以填写多个，本地安装无需配置WebDriverAgent
devicesDict = {
    "SH-SJ-0123": "00008101-001859DE1E38001E",
    "SH-SJ-0182": "00008110-000275943EEB801E",
}


def uinstallIosApp(ipaPackageName):
    # 先卸载
    for name, device in devicesDict.items():
        # 指定设备卸载
        # $ tidevice --udid $UDID uninstall https://example.org/example.ipa
        try:
            # 先停止应用再卸载
            print(f"当前卸载 -- {name}")
            os.system(f"tidevice --udid {device} kill {ipaPackageName}")
            time.sleep(1)
            try:
                dev = connect_device(f"iOS:///http+usbmux://{device}")
                c = wda.Client("http+usbmux://{udid}".format(udid=device))
                c.home()
            except:
                pass
            os.system(f"tidevice --udid {device} uninstall {ipaPackageName}")
        except Exception as e:
            print("失败.......", e, f"当前卸载 -- {name} ")


def installIosApp(ipaPath):
    if isInstallApk:
        print("全部卸载完成......进行安装.....")
        # 再安装
        for name, device in devicesDict.items():
            # 指定设备安装
            # $ tidevice --udid $UDID install https://example.org/example.ipa
            try:
                print(f"当前安装 -- {name}")
                os.system(f"tidevice --udid {device} install {ipaPath}")
            except Exception as e:
                print("失败.......", e, f"当前安装 -- {name} ")

        print("全部安装完成......")


def IOSAppOperation(ipaPath, ipaPackageName, isInstallApk):
    # 先进行卸载
    uinstallIosApp(ipaPackageName)
    # 根据配置判断是否进行安装
    if not isInstallApk:
        print(f"isInstallApk为0,不进行安装，{ipaPackageName} - 全部卸载完毕")
    else:
        installIosApp(ipaPath)


# 示列
if __name__ == '__main__':
    # 是否安装 0 表示不安装只卸载， 1 表示安装
    isInstallApk = 0
    ipaPackageName = "com.demo.ios.apple"  # 奶牛
    ipaPath = "D:\\Y_PythonProject\\xiao-zai-multi-auto-ai-devices\\utils\\apk\\demo.ipa"
    IOSAppOperation(ipaPath, ipaPackageName, isInstallApk)
