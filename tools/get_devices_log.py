# -*- coding: utf-8 -*-
'''
@Time : 2022/9/19 16:50
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : get_devices_log.py
'''
__author__ = "梦无矶小仔"

# -*- coding: utf-8 -*-

# @Time : 2022/9/1 17:39
# @Author : Vincent.xiaozai
# @Email : Lvan826199@163.com
# @File : devices_log.py

from time import sleep
import subprocess,time,os

def log_start(devices,contrl=True):

    if contrl == True:

        print(devices, "日志抓取开始")
        handle = subprocess.Popen("adb -s " + devices + " logcat -c", shell=True)
        sleep(5)
        subprocess.Popen("taskkill /F /T /PID " + str(handle.pid), shell=True)

def log_end(devices,packages, filename,contrl =True):

    import datetime
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dt_ms = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f')
    if contrl == True:
        log_handle = subprocess.Popen(
            "adb -s " + devices + " logcat|findstr " + packages + " > " + filename + "\log_" + dt_ms + devices + ".txt",
            shell=True)
        print("日志路径", filename)
        sleep(10)
        subprocess.Popen("taskkill /F /T /PID " + str(log_handle.pid), shell=True)
        print(devices, "日志抓取结束")
    return filename

def file_exsits(file):
    import os
    from pathlib import Path
    path = Path(file)
    if path.exists():
        pass
    else:
        os.makedirs(path)
    return path

def clear_log():
    s = os.popen("adb devices")
    a = s.read()
    list = a.split('\n')
    deviceList = []
    for temp in list:
        if len(temp.split()) > 1:
            if temp.split()[1] == 'device':
                deviceList.append(temp.split()[0])
    print('本次共扫描出%s个安卓设备' % len(deviceList))
    for devices in deviceList:
        print(devices)
        logcmd = "adb -s " + devices + " logcat -c "
        Poplog = subprocess.Popen(logcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sleep(2)
        Poplog.terminate()
        print(devices,"日志已清理")

def xz_log():
    import os
    import datetime
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dt_ms = datetime.datetime.now().strftime('%Y-%m-%d')
    base_log_path = os.getcwd()
    # 支持在本文件main方法调用调试，logs依然在根目录下的logs下
    if 'utils' in base_log_path:
        if '\\' in base_log_path:
            base_log_path = base_log_path.split('\\utils')[0]
        else:
            base_log_path = base_log_path.split('/utils')[0]
    file = str(file_exsits(f"{base_log_path}/logs/" + dt_ms + "_log"))
    s = os.popen("adb devices")
    a = s.read()
    list = a.split('\n')
    deviceList = []
    for temp in list:
        if len(temp.split()) > 1:
            if temp.split()[1] == 'device':
                deviceList.append(temp.split()[0])
    print('本次共扫描出%s个安卓设备' % len(deviceList))
    for devices in deviceList:
        print(devices)
        ###抓取logcat日志###
        # logcat_filename = file+"\\" + devices +"_"+ dt_ms +"_"+"logcat_log.txt"
        logcat_filename = os.path.join(file,devices +"_"+ dt_ms +"_"+"logcat_log.txt")
        logcat_file = open(logcat_filename, 'w')
        logcmd = "adb -s "+ devices +" logcat "
        Poplog = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
        sleep(2)
        Poplog.terminate()
        ###抓取Radio日志###
        # radio_filename = file+"\\"  + devices + "_" + dt_ms + "_" + "radio_log.txt"
        radio_filename = os.path.join(file , devices + "_" + dt_ms + "_" + "radio_log.txt")
        logcat_file = open(radio_filename, 'w')
        logcmd = "adb -s " + devices + " logcat -b radio "
        Poplog = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
        sleep(2)
        Poplog.terminate()
        ###抓取Main日志###
        # main_filename = file+"\\"  + devices + "_" + dt_ms + "_" + "main_log.txt"
        main_filename = os.path.join( file , devices + "_" + dt_ms + "_" + "main_log.txt")
        logcat_file = open(main_filename, 'w')
        logcmd = "adb -s " + devices + " logcat -b main "
        Poplog = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
        sleep(2)
        Poplog.terminate()
        ###抓取Event日志###
        # event_filename = file+"\\"   + devices + "_" + dt_ms + "_" + "event_log.txt"
        event_filename = os.path.join(file , devices + "_" + dt_ms + "_" + "event_log.txt")
        logcat_file = open(event_filename, 'w')
        logcmd = "adb -s " + devices + " logcat -b event "
        Poplog = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
        sleep(2)
        Poplog.terminate()
        ###抓取kernel日志###
        # kernel_filename = file+"\\"  + devices + "_" + dt_ms + "_" + "kernel_log.txt"
        kernel_filename = os.path.join(file ,devices + "_" + dt_ms + "_" + "kernel_log.txt")
        logcat_file = open(kernel_filename, 'w')
        logcmd = "adb -s " + devices + " cat /proc/kmsg"
        Poplog = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
        sleep(2)
        Poplog.terminate()
        print(devices,"抓取完成")
        print("logcat日志路径:", logcat_filename)
        print("radio日志路径:", radio_filename)
        print("main日志路径:", main_filename)
        print("event日志路径:", event_filename)
        print("kernel日志路径:",kernel_filename)

def ios_log(devices):
    # 还不完善，思路已经有了，我不想写
    print("log开启记录")
    ### 创建文件夹
    from pathlib import Path
    nowtime = time.strftime("%Y-%m-%d", time.localtime())
    path = os.path.join(os.getcwd(), "logs",f"{nowtime}_ioslog")
    path_1 = Path(path)
    if not path_1.exists():
        os.mkdir(path)
    if devices == '4438650ca0ef0073a711ae68b7c5fdc629db9772':  # SH-SJ-0046
        devices_name = 'SH-SJ-0046'
    elif devices == '00008110-000275943EEB801E':  # SH-SJ-0182
        devices_name = 'SH-SJ-0182'
    else:
        devices_name = devices
    logTxtPath = os.path.join(path,f'{devices_name}_log.txt')
    s = subprocess.Popen(f'tidevice -u {devices} syslog >  {logTxtPath}',shell=True)
    print(s.pid)
    return s

def stop_tidevice():
    ...





