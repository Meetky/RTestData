# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :MyProject
 @Date     :2022/3/15 11:13
 @File     :demo2.py
 @Description: 
 @Software :PyCharm
*****************************
"""
import itertools
import time

ll = [{"person": {"name": "kevin", "country": "cn", "traveled": "no"}, "test": 0},
      {"person": {"name": "Alex", "country": "us", "traveled": "yes"}, "test": 0}]


def handle(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(args[0])
        print(f"用时：{time.time() - start}")
        return result

    return wrapper


@handle
def hesuan_test(l):
    time.sleep(2)
    l1 = []
    for i in l:
        for j in i.keys():
            if (j == "test"):
                if (i["test"] == 0):
                    l1.append(i["person"]["name"])
    return l1


@handle
def hs_test(info_list):
    time.sleep(2)
    return [item["person"]["name"]
            for item in info_list if item["test"] == 0
            ]


def test1():
    s = time.time()
    for v1 in range(20):
        for v2 in range(20):
            for v3 in range(20):
                for v4 in range(20):
                    for v5 in range(20):
                        for v6 in range(20):
                            pass
    print(time.time() - s)


def test2():
    s = time.time()
    x = range(20)
    for v1, v2, v3, v4, v5, v6 in itertools.product(x, x, x, x, x, x):
        pass
    print(time.time() - s)


def record_time(func):
    def wrapper(*args):
        print("start time at {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        total = func(*args)
        print("end time at {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        return total
    return wrapper


@record_time
def sum_(*args):
    total = 0
    for ele in args:
        total += ele
    time.sleep(1)
    return total


if __name__ == "__main__":
    # print(hesuan_test(ll))
    # print(hs_test(ll))
    print(sum_(1, 2, 3))
