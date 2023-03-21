# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :MyProject
 @Date     :2022/1/20 14:33
 @File     :test.py
 @Description:
 @Software :PyCharm
*****************************
"""

import os
import sys
import socket


def get_ip():
    # 获取主机名称
    host_name = socket.gethostname()
    # 获取主机ip
    # host = socket.gethostbyname(host_name)
    host = socket.gethostbyname_ex(host_name)[-1][-1]
    return host


def share(host, path):
    sysname = sys.platform
    if "win" in sysname:
        res = handle_win_path(path)
        # 指定文件夹，执行共享操作
        print(f"共享文件夹的路径为：{res[-1]}")
        print(f"共享开启，请在局域网内访问：http://{host}:{1688}")
        if res[0]:
            # 与执行程序目录相同的情况
            os.system(r"cd {} && python -m http.server 1688".format(res[-1]))
        else:
            # 与执行程序目录不同的情况
            os.system(r"{}: && cd {} && python -m http.server 1688".format(res[1], res[-1]))
    else:
        os.system(r"cd {} && python -m http.server 1688".format(path))
        pass


def handle_win_path(path):
    """路径处理"""
    home_path = path.split(":")[0]
    if path.split(":")[-1] is "":
        path = path + "\\"
    current_path = os.path.abspath(__file__).split(":")[0]
    if home_path == current_path:
        return True, 0, path
    return False, home_path, path


def main():
    while True:
        path = str(input(r"请输入共享文件夹路径(如：D:\):"))
        code = os.system(r"cd {}".format(path))
        if code == 0:
            break
        print("输入格式错误，注意英文状态字符")
    share(get_ip(), path)


if __name__ == '__main__':
    main()
