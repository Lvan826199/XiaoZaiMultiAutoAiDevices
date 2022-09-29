# -*- coding: utf-8 -*-

# @Time : 2022/6/21 18:08
# @Author : Vincent.xiaozai
# @Email : Lvan826199@163.com
# @File : pocoCommonMethod.py

#################################################### 元素操作
# 可以自己拓展
#### 重跑机制
import time
from datetime import datetime


def rerun(times: int):
    def wapper(func):
        def inner(*args,**kwargs):
            for i in range(times):
                result = func(*args,**kwargs)
                if result:
                    break
        return inner
    return wapper

#===========判断元素是否存在=================
def isElementExistAndClick(poco,element,method="N"):
    '''元素存在则点击,否则直接跳过'''
    if method == 'N':
        elementInfo = poco(element)
    elif method == 'text':
        elementInfo = poco(text=element)
    elif method == 'texture':
        elementInfo = poco(texture=element)
    else:
        print(f"{method}方法还未加入,请加入")
        elementInfo = None
    time.sleep(1)
    if elementInfo:
        while True:
            if elementInfo.exists():
                print(element+"元素存在")
                elementInfo.click()
                print(element + "元素点击成功")
                break
            else:
                print(element + "元素不存在")

@rerun(3)
def longElementExistAndClick(element)-> bool:
    '''长元素的定位点击'''
    if element.exists():
        print(element , "元素存在")
        element.click()
        print(element , "元素点击成功")
        return True
    else:
        print(element , "元素不存在")
        return False

@rerun(3)
def longElementExistTextAndClick(element,jugeText) -> bool:
    '''长元素获取对应的text并判断是否存在，存在则点击'''
    if element.exists():
        print(element , "元素存在")
        #获取元素的text
        textMsg = element.get_text().strip()
        if textMsg == jugeText:
            element.click()
            print(f"---{element}---元素点击成功")
            return True
    else:
        print(element , "元素不存在")
        return False

@rerun(3)
def testRerun() -> bool:
    from random import randint
    i = randint(0,5)
    if i == 3:
        print(f"------{i}----成功-")
        return True
    else:
        print(f"--------{i}----失败------")
        return False

#################################滑动操作##############################
from airtest.core.api import *
def swipe_up(poco_U):
    '向上滑动屏幕'
    x, y = poco_U.get_screen_size()
    swipe((x / 2, y * 0.8), (x / 2, y * 0.2), duration=0.5)  # start(x1,y1) to (x2,y2) # 向上滑动up，y从大到小

def swipe_up_small(poco_U):
    '向上小幅度滑动屏幕'
    x, y = poco_U.get_screen_size()
    swipe((x / 2, y * 0.7), (x / 2, y * 0.4), duration=0.5)  # start(x1,y1) to (x2,y2) # 向上滑动up，y从大到小

def swipe_up_quit(poco_U):
    '向上小幅度滑动屏幕'
    x, y = poco_U.get_screen_size()
    swipe((x / 2, y * 0.9), (x / 2, y * 0.2), duration=1)  # start(x1,y1) to (x2,y2) # 向上滑动up，y从大到小

def swipe_down(poco_U):
    '向下滑动屏幕'
    x, y = poco_U.get_screen_size()
    swipe((x / 2, y * 0.2), (x / 2, y * 0.8), duration=0.5)  # start(x1,y1) to (x2,y2) # 向下滑动down，y从小到大

def swipe_down_small(poco_U):
    '向下小幅度滑动屏幕'
    x, y = poco_U.get_screen_size()
    swipe((x / 2, y * 0.4), (x / 2, y * 0.7), duration=0.5)  # start(x1,y1) to (x2,y2) # 向下滑动down，y从小到大

def swipe_left(poco_U):
    '向左滑动屏幕'
    x, y = poco_U.get_screen_size()
    swipe((x * 0.8, y / 2), (x * 0.2, y / 2), duration=0.5)  # start(x1,y1) to (x2,y2) # 向左滑动left，x从大到小

def swipe_left_small(poco_U):
    '向左小幅度滑动屏幕'
    x, y = poco_U.get_screen_size()
    swipe((x * 0.7, y / 2), (x * 0.4, y / 2), duration=0.5)  # start(x1,y1) to (x2,y2) # 向左滑动left，x从大到小


def swipe_right(poco_U):
    '向右滑动屏幕'
    x, y = poco_U.get_screen_size()
    print(x,y)
    swipe((x * 0.2, y / 2), (x * 0.8, y / 2), duration=0.5)  # start(x1,y1) to (x2,y2) # 向右滑动right，x从小到大

def swipe_right_small(poco_U):
    '向右小幅度滑动屏幕'
    x, y = poco_U.get_screen_size()
    swipe((x * 0.4, y / 2), (x * 0.7, y / 2), duration=0.5)  # start(x1,y1) to (x2,y2) # 向右滑动right，x从小到大

def __hello():
    '''测试'''
    from poco.drivers.ios import iosPoco
    device = connect_device("ios:///http+usbmux://4438650ca0ef0073a711ae68b7c5fdc629db9772")
    poco_U = iosPoco(device)
    for i in range(30):
        swipe_right(poco_U)

################################################# unittest重跑机制
# coding=utf-8
import sys
import functools
import traceback
import inspect
import unittest

def retry(target=None, max_n=1, func_prefix="test"):
    """
    一个装饰器，用于unittest执行测试用例出现失败后，自动重试执行

# example_1: test_001默认重试1次
class ClassA(unittest.TestCase):
    @retry
    def test_001(self):
        raise AttributeError


# example_2: max_n=2,test_001重试2次
class ClassB(unittest.TestCase):
    @retry(max_n=2)
    def test_001(self):
        raise AttributeError


# example_3: test_001重试3次; test_002重试3次
@retry(max_n=3)
class ClassC(unittest.TestCase):
    def test_001(self):
        raise AttributeError

    def test_002(self):
        raise AttributeError


# example_4: test_102重试2次, test_001不参与重试机制
@retry(max_n=2, func_prefix="test_1")
class ClassD(unittest.TestCase):
    def test_001(self):
        raise AttributeError

    def test_102(self):
        raise AttributeError


    :param target: 被装饰的对象，可以是class, function
    :param max_n: 重试次数，没有包含必须有的第一次执行
    :param func_prefix: 当装饰class时，可以用于标记哪些测试方法会被自动装饰
    :return: wrapped class 或 wrapped function
    """

    def decorator(func_or_cls):
        if inspect.isfunction(func_or_cls):
            @functools.wraps(func_or_cls)
            def wrapper(*args, **kwargs):
                n = 0
                while n <= max_n:
                    try:
                        n += 1
                        func_or_cls(*args, **kwargs)
                        return
                    except Exception:  # 可以修改要捕获的异常类型
                        if n <= max_n:
                            trace = sys.exc_info()
                            traceback_info = str()
                            for trace_line in traceback.format_exception(trace[0], trace[1], trace[2], 3):
                                traceback_info += trace_line
                            print(traceback_info)  # 输出组装的错误信息
                            args[0].tearDown()
                            args[0].setUp()
                        else:
                            raise

            return wrapper
        elif inspect.isclass(func_or_cls):
            for name, func in list(func_or_cls.__dict__.items()):
                if inspect.isfunction(func) and name.startswith(func_prefix):
                    setattr(func_or_cls, name, decorator(func))
            return func_or_cls
        else:
            raise AttributeError

    if target:
        return decorator(target)
    else:
        return decorator


class Retry(object):
    """
    类装饰器, 功能与Retry一样


# example_1: test_001默认重试1次
class ClassA(unittest.TestCase):
    @Retry
    def test_001(self):
        raise AttributeError


# example_2: max_n=2,test_001重试2次
class ClassB(unittest.TestCase):
    @Retry(max_n=2)
    def test_001(self):
        raise AttributeError


# example_3: test_001重试3次; test_002重试3次
@Retry(max_n=3)
class ClassC(unittest.TestCase):
    def test_001(self):
        raise AttributeError

    def test_002(self):
        raise AttributeError


# example_4: test_102重试2次, test_001不参与重试机制
@Retry(max_n=2, func_prefix="test_1")
class ClassD(unittest.TestCase):
    def test_001(self):
        raise AttributeError

    def test_102(self):
        raise AttributeError

    """

    def __new__(cls, func_or_cls=None, max_n=1, func_prefix="test"):
        self = object.__new__(cls)
        if func_or_cls:
            self.__init__(func_or_cls, max_n, func_prefix)
            return self(func_or_cls)
        else:
            return self

    def __init__(self, func_or_cls=None, max_n=1, func_prefix="test"):
        self._prefix = func_prefix
        self._max_n = max_n

    def __call__(self, func_or_cls=None):
        if inspect.isfunction(func_or_cls):
            @functools.wraps(func_or_cls)
            def wrapper(*args, **kwargs):
                n = 0
                while n <= self._max_n:
                    try:
                        n += 1
                        func_or_cls(*args, **kwargs)
                        return
                    except Exception:  # 可以修改要捕获的异常类型
                        if n <= self._max_n:
                            trace = sys.exc_info()
                            traceback_info = str()
                            for trace_line in traceback.format_exception(trace[0], trace[1], trace[2], 3):
                                traceback_info += trace_line
                            print(traceback_info)  # 输出组装的错误信息
                            args[0].tearDown()
                            args[0].setUp()
                        else:
                            raise

            return wrapper
        elif inspect.isclass(func_or_cls):
            for name, func in list(func_or_cls.__dict__.items()):
                if inspect.isfunction(func) and name.startswith(self._prefix):
                    setattr(func_or_cls, name, self(func))
            return func_or_cls
        else:
            raise AttributeError


if __name__ == '__main__':
    __hello()