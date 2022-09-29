# -*- coding: utf-8 -*-
'''
@Time : 2022/9/19 11:48
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : IOSAppOperate.py
'''
__author__ = "梦无矶小仔"
import sys
sys.dont_write_bytecode = True
from airtest.core.api import *

########################### 182  账号登录，app下载等步骤
class SH_182():
    def check_acount_ios14(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        c.close()
        c.app_stop("com.apple.Preferences")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.Preferences")
                App_Store = c(type="Cell", name="App Store", label="App Store",
                              enabled="true")
                App_Store_sign = 0
                while 1:
                    print("寻找ios14设备+的App Store.....")
                    for i in range(2):
                        swipe([0.5, 0.6], [0.5, 0.4])
                        if App_Store.visible:
                            App_Store_sign = 1
                            print("ios14设备+ 的  App Store寻找到了")
                            break
                    if App_Store.visible:
                        print("寻找ios14设备+ 的  App Store寻找到了")
                        break
                    if App_Store_sign == 1:
                        pass
                    else:
                        if App_Store.visible:
                            print("iTunes Store 与 App Store寻找到了")
                            break
                App_Store.click()
            for i in range(3):
                print('滑到底部')
                swipe([0.5, 0.7], [0.5, 0.3])
                time.sleep(2)
            c(type="Cell", enabled="true", visible="true")[-3].wait(timeout=280)
            if c(type="Cell", enabled="true", visible="true")[-3].exists:
                aount = c(type="Cell", enabled="true", visible="true")[-3].label
                print("=======================================")
                print("=================", aount, "============")
                print("=======================================")
                if aount == "登录":
                    c(type="Cell", enabled="true", visible="true")[-3].click()
                    c(value="电子邮件或电话", label="").set_text(acount)  ##账号
                    # 点击登录再输入密码
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    c(value="密码", label="").set_text(pwd)  ##密码
                    time.sleep(1)
                    # 再次点击登录
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    sleep(10)
                else:
                    if len(aount.split('ID：')) > 0:
                        test_aount = aount.split('ID：')[1]
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print("账号不正确，退出重新登录")
                            c(type="Cell", enabled="true", visible="true")[-3].click()  ##点击账号处，弹出退出页面
                            c(type="Button", name="退出登录", label="退出登录", enabled="true",
                              visible="true").click()  ##点击退出登录按钮
                            time.sleep(8)
                            c(type="Cell", enabled="true", visible="true")[-3].click()  # 再次点击登录进行登录
                            c(value="电子邮件或电话", label="").set_text(acount)  ##账号
                            # 点击登录再输入密码
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            c(value="密码", label="").set_text(pwd)  ##密码
                            time.sleep(1)
                            # 再次点击登录
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            sleep(10)
            c.app_stop("com.apple.Preferences")
            c.close()
        except Exception as e:
            print(e)

    def loginAppStore(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        print("----")
        c.close()
        c.app_stop("com.apple.AppStore")
        print("-----------------------------------")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.AppStore")
                time.sleep(5)
                continueButton = c(type='Button', name='继续', label='继续', enabled='true')
                continueButton_182 = c(type='StaticText', name='继续', label='继续', enabled='true')
                sayAfterButton_182 = c(type='Button', name='以后再说', label='以后再说', enabled='true')

                if sayAfterButton_182.exists:
                    print('----------点击以后再说-----------')
                    sayAfterButton_182.click()

                if continueButton.exists:
                    print('----------点击继续-----------')
                    continueButton.click()

                if continueButton_182.exists:
                    print('----------点击 sh-sj-182设备 继续-----------')
                    continueButton_182.click()
                print("--------------点击我的账户--------------")
                myAccountButton = c(type="Button", label="我的帐户",
                                    enabled="true")
                myAccountButton.click()
                time.sleep(3)
                # e = c(enabled="true", visible="true")[0]
            # 判断是否登录
            c(type="StaticText", enabled="true", visible="true").wait(timeout=280)
            if c(type="StaticText", enabled="true", visible="true").exists:
                AppleID = c(type="Cell", enabled="true", visible="true").label
                print("=======================================")
                print("=================", AppleID, type(AppleID), "============")
                print("=======================================")
                if AppleID == None:
                    # 进行登录
                    c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(acount)  ##账号
                    c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(pwd)  ##密码
                    c(type="Cell", label="登录", enabled="true", visible="true").click()  # 点击登录
                    sleep(10)
                else:
                    if len(AppleID.split(',')) > 0:
                        test_aount = AppleID.split(',')[1].strip()
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print(f"账号不正确，退出重新登录：{test_aount}")
                            while True:
                                print('--------检查退出登录是否存在-------')
                                try:
                                    c(type='StaticText', name='退出登录', visible='true').click()
                                    time.sleep(5)
                                    print("--------------------点击退出登录成功----------------")
                                    break
                                except:
                                    print("---------滑动查找退出登录-----------")
                                    swipe([0.5, 0.7], [0.5, 0.3])  # 向上滑
                                    time.sleep(1)
                                    # c.close()
                                    # e.scroll('down')

                            for i in range(4):
                                print("---------向上滑动-----------")
                                swipe([0.5, 0.3], [0.5, 0.7])
                                time.sleep(1)
                            # 进行登录
                            c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(
                                acount)  ##账号
                            c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(
                                pwd)  ##密码
                            c(type="Cell", label="登录", enabled="true",
                              visible="true").click()  # 点击登录
                            sleep(10)

            ### 如果没有双重认证的,则需要进行确认
            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    print("认证完毕或不需要认证，退出！")
                    break
            c.app_stop("com.apple.AppStore")
            c.close()
        except Exception as e:
            print(e)

    def App_download(self, c, name):
        c.app_stop("com.apple.TestFlight")
        c.app_start("com.apple.TestFlight")
        if c(type='Button', name='Continue Button').exists:
            c(type='Button', name='Continue Button').click()
        sleep(8)
        sroll = c(enabled="true", visible="true")

        app_name = c(type="Cell", name=name)
        n = 0
        while 1:
            n += 1
            if n <= 6:
                if app_name.exists:
                    print("已找到")
                    break
                else:
                    swipe([0.5, 0.6], [0.5, 0.4])
                    print("向下滑")
            if 5 < n < 13:
                if app_name.exists:
                    break
                else:
                    swipe([0.5, 0.4], [0.5, 0.6])
                    print("向上滑")
            if n > 10:
                n = 0

        # for i in range(1):
        #     sroll.scroll('up')
        # StaticText
        install_Button = c(type="Button", name="安装")
        install_Button_2 = c(type="Button", name="INSTALL")
        open_Button = c(type="Button", name="打开")
        open_Button_2 = c(type="Button", name="OPEN")
        while 1:
            ##点击目标App
            print("安装中...")
            if app_name.exists:
                app_name.click()
            else:
                print("App不在App不在App不在")
            print("验证安装按钮在不在", install_Button.exists)
            print("验证英文安装按钮在不在", install_Button_2.exists)
            time.sleep(5)
            if install_Button.exists is True:
                ##点击安装按钮
                print("如果安装按钮在则点击", install_Button.exists)
                install_Button.click()

            if install_Button_2.exists is True:
                ##点击安装按钮
                print("如果英文按钮在则点击", install_Button_2.exists)
                install_Button_2.click()

            if open_Button_2.exists:
                print("已经安装成功")
                break

            if open_Button.exists:
                print("已经安装成功")
                break
        c.app_stop("com.apple.TestFlight")
        c.close()
