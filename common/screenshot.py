# -*- coding: utf-8 -*-
'''
@Time : 2022/9/19 13:42
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : screenshot.py
'''
__author__ = "梦无矶小仔"

from datetime import datetime
from pathlib import Path
from airtest.core.android.adb import ADB
from airtest.core.api import *

adb = ADB().adb_path
reportpath = os.path.join(os.getcwd(), "Reports")
imagesPath = os.path.join(reportpath, "images")


def makeImagesFolder():
    path_1 = Path(imagesPath)
    if not path_1.exists():
        os.mkdir(imagesPath)
    return imagesPath


# 日志截图
def iosScreenshot(devices,action):
    # 对设备的uuid进行重命名，这个方法可以根据自己需求自行更改
    if devices == '4438650ca0ef0073a711ae68b7c5fdc629db9772':  # SH-SJ-0046
        devices_name = 'SH-SJ-0046'
    elif devices == '00008110-000275943EEB801E':  # SH-SJ-0182
        devices_name = 'SH-SJ-0182'
    elif devices == 'cc6aecac0cbaf3e0a9aef1e8fcb848cd8292461b':  # BJ-SJ-0011
        devices_name = 'BJ-SJ-0011'
    else:
        devices_name = devices
    imagesPath = makeImagesFolder()
    nowtime = datetime.now().strftime("%Y%m%d%H%M%S")
    path = imagesPath + "\\" +  str(nowtime) +  "_" +  devices_name + "_" + action+ ".jpg"
    snapshot(filename=path,msg=action, quality=90, max_size=800)
    hrefPath = '\\'.join(path.split('\\')[-2:])
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),"<img src='" + hrefPath + "' height='500px' />")


#################################poco截图操作##############################
def screenShot(poco,imgPath):
    '''
    截图
    :param imgPath:截图保存路径
    :return:  截图名字
    '''
    from base64 import b64decode
    b64img, fmt = poco.snapshot() #通过snapshot进行截图
    open('{}.{}'.format(imgPath,fmt), 'wb').write(b64decode(b64img)) #写入以图片的形式存储
    imgName = imgPath+'.'+fmt
    return imgName

### android使用airtest原生截图无效可使用这个方法
# 此方法兼容接入poco下的ios，android,unity,UE4，Cocos-lua,Cocos-C++,Cocos-js
def screenShotHref(poco,testName):
    '''
    生成报告的截图链接
    '''
    nowTime = datetime.now().strftime("%Y%m%d%H%M%S")
    path = makeImagesFolder()
    imgPath = path + f'\\{testName}_' + nowTime
    path_2 = screenShot(poco=poco,imgPath=imgPath)  # 不需要带图片的后缀
    href = '\\'.join(path_2.split('\\')[-2:])
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), "<img src='" + href + "' height='500px' />")


if __name__ == '__main__':
    ...
    # 示例
    # from airtest.core.api import *
    # device = connect_device('android://127.0.0.1:5037/77095c4c')
    # from poco.drivers.unity3d import UnityPoco
    # poco = UnityPoco(device=device)
    # screenShotHref(poco,'示例截图_1')
