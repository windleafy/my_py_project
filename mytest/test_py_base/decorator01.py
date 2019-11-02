#!/usr/bin/env python
"""decorator01"""

# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 14:59
# @Author  : Wind
# @Des     :
# @Software: PyCharm
import functools
import logging


def use_logging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        func()
        logging.warning("%s is ending" % func.__name__)
        return func  # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()

    return wrapper


@use_logging
def foo():
    print('i am foo')


foo()  # 执行foo()就相当于执行 wrapper()
print('=====1' + '=' * 70)


# 构建装饰器
def use_logging(func):
    @functools.wraps(func)
    def decorator():
        print("%s called" % func.__name__)
        result = func()
        print("%s end" % func.__name__)
        return result

    return decorator


# 使用装饰器
@use_logging
def test01():
    return 1


# 测试用例
print(test01())
print(test01.__name__)
print('=====2' + '=' * 70)


# 构建装饰器
def use_logging(func):
    @functools.wraps(func)
    def decorator(a, b):
        print("%s called" % func.__name__)
        result = func(a, b)
        print("%s end" % func.__name__)
        return result

    return decorator


# 使用装饰器
@use_logging
def test01(a, b):
    print("in function test01, a=%s, b=%s" % (a, b))
    return 1


# 测试用例
print(test01(1, 2))
print('=====3装饰带两个参数的函数' + '=' * 70)


# 构建装饰器
def use_logging(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        print("%s called" % func.__name__)
        result = func(*args, **kwargs)
        print("%s end" % func.__name__)
        return result

    return decorator


# 使用装饰器
@use_logging
def test01(a, b):
    print("in function test01, a=%s, b=%s" % (a, b))
    return 1


# 使用装饰器
@use_logging
def test02(a, b, c, d):
    print("in function test02, a=%s, b=%s, c=%s, d=%s" % (a, b, c, d))
    return 1


# 测试用例
print(test01(1, 2))
print(test02(1, 2, c=3, d=4))
print('=====4装饰带任意参数的函数' + '=' * 70)


# 构建装饰器
def params_chack(a_type, b_type):
    def _outer(func):
        @functools.wraps(func)
        def _inner(a, b):
            assert isinstance(a, a_type) and isinstance(b, b_type)
            return func(a, b)

        return _inner

    return _outer


# 使用装饰器  带参数的装饰器
@params_chack(int, (list, tuple))
def test03(a, b):
    print("in function test03, a=%s, b=%s" % (a, b))
    return 1


# 测试用例
print(test03(1, [2, 3]))  # 参数正确
# print(test03(1, 2))  # 参数错误
print('=====5装饰器带有两个参数，进行参数检查' + '=' * 70)


# 构建装饰器
def params_chack(*types, **kw_types):
    def _outer(func):
        @functools.wraps(func)
        def _inner(*args, **kwargs):
            result = [isinstance(_param, _type) for _param, _type in zip(args, types)]
            assert all(result), "params_chack: invalid parameters"
            result = [isinstance(kwargs[_param], kw_types) for _param in kwargs if _param in kw_types]
            assert all(result), "params_chack: invalid parameters"
            return func(*args, **kwargs)

        return _inner

    return _outer


# 使用装饰器
@params_chack(int, str, c=(int, str))
def test04(a, b, c):
    print("in function test04, a=%s, b=%s, c=%s" % (a, b, c))
    return 1


# 测试用例
print(test04(1, "str", 1))  # 参数正确
print(test04(1, "str", "abc"))  # 参数正确
# print(test04("str", 1, "abc"))  # 参数错误
print('=====6装饰器带有任意参数，进行参数检查' + '=' * 70)


# 使用装饰器
class ATest(object):
    @params_chack(object, int, str)
    def test(self, a, b):
        print("in function test of ATest, a=%s, b=%s" % (a, b))
        return 1


# 测试用例
a_test = ATest()
a_test.test(1, "str")  # 参数正确
# a_test.test("str", 1)  # 参数错误
print('=====7装饰器检查类中的函数参数' + '=' * 70)


@use_logging
@params_chack(int, str, (list, tuple))
def test05(a, b, c):
    print("in function test05, a=%s, b=%s, c=%s" % (a, b, c))
    return 1


# 测试用例
print(test05(1, "str", [1, 2]))  # 参数正确
print(test05(1, "str", (1, 2)))  # 参数正确
# print(test05(1, "str", "str1str2"))    # 参数错误
print('=====8使用多个装饰器' + '=' * 70)


# 构建装饰器类
class Decorator(object):
    def __init__(self, func):
        self.func = func
        return

    def __call__(self, *args, **kwargs):
        print("%s called" % self.func.__name__)
        result = self.func(*args, **kwargs)
        print("%s end" % self.func.__name__)
        return result


# 使用装饰器
@Decorator
def test06(a, b, c):
    print("in function test06, a=%s, b=%s, c=%s" % (a, b, c))
    return 1


# 测试用例
print(test06(1, 2, 3))
print('=====9装饰器类' + '=' * 70)


# 构建装饰器类
class ParamCheck(object):

    def __init__(self, *types, **kwtypes):
        self.types = types
        self.kwtypes = kwtypes
        return

    def __call__(self, func):
        @functools.wraps(func)
        def _inner(*args, **kwargs):
            result = [isinstance(_param, _type) for _param, _type in zip(args, self.types)]
            assert all(result), "params_chack: invalid parameters"
            result = [isinstance(kwargs[_param], self.kwtypes) for _param in kwargs if _param in self.kwtypes]
            assert all(result), "params_chack: invalid parameters"
            return func(*args, **kwargs)

        return _inner


# 使用装饰器
@ParamCheck(int, str, (list, tuple))
def test07(a, b, c):
    print("in function test06, a=%s, b=%s, c=%s" % (a, b, c))
    return 1


# 测试用例
print(test07(1, "str", [1, 2]))  # 参数正确
print(test07(1, "str", (1, 2)))  # 参数正确
# print(test07(1, 2, (1, 2)))  # 参数错误
print('=====10带参数的装饰器类' + '=' * 70)


# 实例: 函数缓存
def funccache(func):
    cache = {}

    @functools.wraps(func)
    def _inner(*args):
        if args not in cache:
            print('no cache, do func')
            cache[args] = func(*args)
        return cache[args]

    return _inner


# 使用装饰器
@funccache
def test08(a, b, c):
    # 其他复杂或耗时计算
    return a + b + c


print(test08(10, 20, 30))
print(test08(10, 20, 30))
print(test08(50, 20, 30))

print('=====11函数缓存装饰器' + '=' * 70)
