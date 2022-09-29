# -*- coding: utf-8 -*-
'''
@Time : 2022/9/14 10:53
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : index.py
'''
__author__ = "梦无矶小仔"

from multiprocessing import Process
from airtest.core.error import *
from poco.exceptions import *
from airtest.core.api import *
from utils import RunTestCase
from utils.MultiDevices import MultiDevices
from utils.readConfig import *
import traceback


index_print = print
def print(*args, **kwargs):
    index_print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)

'''

'''

def main():
    #直接读取ini文件中TestCase对应的设备，使用者可以根据自己的情况进行重写
    # 如直接通过命令获取ios的uuid，再匹配上对应的TestCase进行运行即可
    allDevicesList = MultiDevices().getdevices()
    print(f'当前所连接的设备列表:{allDevicesList}')
    reportpath = os.path.join(os.getcwd(), "Reports")
    # 没有Report目录时自动创建
    if not os.path.exists(reportpath):
        os.mkdir(reportpath)
    print("测试开始")
    # 获取TestCase下需要启动的设备列表
    runDevicesList = list(getAllTestCase().keys()) #拿到的设备名称全是小写，全是config的锅
    print('当前标记的设备列表：',runDevicesList)
    # 判定配置表里面TestCase下的设备是否在线
    for device in runDevicesList:
        if device not in [x.lower() for x in allDevicesList]:
            print(f'\033[31m{device}设备不在线，可能未开启WebDriverAgent服务，请在tools文件夹下启动start_ios_devices或检查设备是否配置好相关环境!\033[0m')

    # 只有在TestCase配置项下配置了,并且在线的设备才会进行运行
    d = dict(zip(range(len(allDevicesList)), allDevicesList))
    for k, v in d.items():
        if v.lower() not in runDevicesList:
            d[k] = []
    finalDevicesList = [v for k, v in d.items() if v]
    print('等待跑用例的设备列表:',finalDevicesList)


    if finalDevicesList:
        try:
            print("启动进程池")
            pool_list = []
            # 根据设备列表去循环创建进程，对每个进程调用enter_processing 方法
            for i in range(len(finalDevicesList)):
                start = time.localtime()
                MD = MultiDevices(finalDevicesList[i])
                if MD.get_androidversion() < 3:
                    print("设备{}的安卓版本低于5，不支持当前安卓版本！".format(MD.get_mdevice()))
                    continue
                pools = Process(target=enter_processing,args=(i,MD,start,))
                pool_list.append(pools)
            print("---------------------------------------------")
            print(f"当前线程池列表：{pool_list}")
            print("---------------------------------------------")
            for pool in pool_list:
                pool.start()
            for pool in pool_list:
                pool.join()
            print("进程回收完毕")
            print("测试结束")
        except AirtestError as ae:
            print(f"Airtest发生错误:{ae}")
        except PocoException as pe:
            print(f"Poco发生错误:{pe}")
        except Exception as e:
            print(f"发生未知错误:{e}")
    else:
        print("未找到设备，测试结束")



'''
调用TestCase中的测试用例进行测试的主功能函数
'''
from airtest.cli.parser import cli_setup
def enter_processing(processNo,MD,start):
    devices = MD.get_mdevice() # 获取当前连接的设备名字
    print("进入第{}个进程,devicename={}".format(processNo,devices))
    try:
        startflag = "Success"
        #调用airtest的各个方法连接设备 以下为示例（不同的设备有些连接方式是不能互通的，具体的根据自己的实际情况进行选择）
        ####### 以下为Android设备  ##########
        if devices == "HA0Y7AUR":
            if not cli_setup():
                auto_setup(__file__, logdir=True, devices=["Android://127.0.0.1:5037/HA0Y7AUR",])
        elif devices == "66J5T18A28047220":
            connect_device("Android:///" + devices)
        elif devices == "04157df4d5a71515":
            connect_device("Android:///" + devices + "?touch_method=ADBTOUCH")
        elif devices == "R28M405TJBX":
            connect_device("Android:///" + devices + "?cap_method=JAVACAP")
        elif devices == "2684c2b0":
            connect_device("Android:///" + devices + "?cap_method=JAVACAP&&touch_method=ADBTOUCH")

#########################   以下为ios设备

        ###########SH-SJ-0123
        elif devices == "00008101-001859DE1E38001E":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://00008101-001859DE1E38001E", ])
        #### SH-SJ-0186
        elif devices == "00008030-001E19021A42802E":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                       devices=["ios:///http+usbmux://00008030-001E19021A42802E", ])
        else:
            print(f'{devices}未做处理，请在index文件下添加该设备！')
            startflag = "Fail"

        time.sleep(15)
        auto_setup(__file__)
        print("设备{}连接成功".format(devices))

        #应用启动成功则开始运行用例
        if (startflag=="Success"):
            RunTestCase.RunTestCase(MD, start)    ################  用例在这运行
            print("{}完成测试".format(devices))
        else:
            print("{}未运行测试。".format(devices))
    except Exception as e:
        print( "连接设备{}失败".format(devices)+ traceback.format_exc())








