# -*- coding: utf-8 -*-
'''
@Time : 2022/9/14 15:59
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : readConfig.py
'''
__author__ = "梦无矶小仔"


import os,inspect,configparser
import time
from configparser import NoSectionError
'''
读取配置文件
增加了新增及删除对应的section和option，但不建议使用；
configparser库本身存在问题，在写入和删除时会丢失所有注释，建议使用其他方式写入；
或者说注释丢失没有影响的话，就可以随意使用。
'''

# 获取当前文件的上层路径
parentPath = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".")
# 获取当前项目的根路径
rootPath = os.path.abspath(os.path.dirname(parentPath) + os.path.sep + ".")
# 获取config.ini文件路径
# configPath = rootPath + "\settings\config.ini"
configPath = os.path.join(rootPath , "settings","config.ini")
# 初始化配置文件
configFile = configparser.ConfigParser()
configFile.read(configPath, encoding='UTF-8-sig')

# 获取TestCaseforDevice下的所有设备uuid及对应的用例，多个用例用逗号分隔
def getAllTestCase():
    '''
    :return: 字典组合的{'device1':'case1,case1_1','device2':'case2'}
    '''
    selectDevicesList = configFile.options('TestCaseforDevice')
    selectTestCaseList = []
    for i in selectDevicesList:
        selectTestCaseList.append(configFile.get('TestCaseforDevice',i))
    device_case_dict = dict(zip(selectDevicesList,selectTestCaseList))
    return device_case_dict

# 获取指定的用例文件夹名称
def getSpCaseFolder():
    getCaseFolder = configFile.options('TestCaseSpFolder')
    getSpCaseFolderList = []
    for i in getCaseFolder:
        try:
            if configFile.getint('TestCaseSpFolder',i) == 1:
                getSpCaseFolderList.append(i)
        except:pass
    return getSpCaseFolderList

#获取设备列表
def get_devicesList():
    devicesList = []
    get_devicesList = configFile.get('config','deviceslist')
    devices = get_devicesList.split(',')
    for i in devices:
        devicesList.append(i)
    return devicesList



#写配置文件
def addConfig(section,option,value):
    if  option!="" and value!="":
        if not configFile.has_section(section):
            configFile.add_section(section)
        configFile.set(section,option,value)
        configFile.write(open(configPath, "w"))


#删除配置文件下某个setion的所有内容
def delSectionConfig(section):
    if configFile.has_section(section):
        configFile.remove_section(section)
        configFile.write(open(configPath, "w"))
    else:
        raise f"{section}不存在!"

#删除配置文件下setion下的某个option
def delOptionConfig(section,option):
    if configFile.has_option(section,option):
        configFile.remove_option(section,option)
        configFile.write(open(configPath, "w"))
    else:
        raise f"填写的{option}不存在于{section}下!"

if __name__ == '__main__':
    # print(addConfig("test","xiaozai",'666'))
    print(getAllTestCase())
    # print(getAllTestCase()['00008110-000275943eeb801e'])
