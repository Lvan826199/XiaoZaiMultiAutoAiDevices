# -*- coding: utf-8 -*-

# @Time : 2022/9/19 16:08
# @Author : Vincent.xiaozai
# @Email : Lvan826199@163.com
# @File : imageElePath.py

from airtest.core.api import *

'''
imageElePath.py文件用于存储airtest中对图像识别的图片，其他文件可以直接引用此文件使用对应的图片
图片存储在项目根目录的imageFiles文件夹下
如果有多个项目,可以在imageFiles下创建对应项目文件夹,具体可以根据需求进行改进
此文件只做示例
'''
                                                    ######################
                            ############################            ###############################
                            ############################  图片存储  ###############################
                            ############################           ###############################
                                                   #######################
# 登录 继续
facebook_continue = Template(r"../imageFiles/FaceBook/tpl1662538211709.png", record_pos=(0.171, 0.664), resolution=(1284, 2778))


