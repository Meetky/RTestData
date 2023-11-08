# -*- coding: utf-8 -*-
# @Project  :MyProject
# @File     :create_particle
# @Date     :2021/7/20 13:23
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
import copy
import random

from my_api.demo.data_base import DataBase


class Generation3DData(DataBase):
    def __init__(self):
        super().__init__()
        self.data = {
            "id": None,
            "coordinate": {}
        }
        self.data_ = {
            "id": None,
            "position": {}
        }

    def particle(self, num):
        for n in range(num):
            data = copy.deepcopy(self.data)
            data["id"] = n
            data["coordinate"]["lat"], data["coordinate"]["lng"] = self.generation_lat_lng_bj()
            self.page_data["data"].append(data)

        self.page_data["total"] = num
        return self.page_data

    def hot_chart(self, num):
        for n in range(num):
            data = copy.deepcopy(self.data)
            data["id"] = n
            data["count"] = str(random.randint(1, 1000))
            data["coordinate"]["lat"], data["coordinate"]["lng"] = self.generation_lat_lng_bj()
            self.page_data["data"].append(data)

        self.page_data["total"] = num
        return self.page_data

    def trajectory(self, num):
        for n in range(num):
            data = copy.deepcopy(self.data_)
            data["id"] = n
            data["position"]["x"], data["position"]["y"], data["position"]["z"] = self.generation_x_y_z()
            self.page_data["data"].append(data)
        self.page_data["total"] = num
        return self.page_data


if __name__ == '__main__':
    gen = Generation3DData()
    print(gen.trajectory(3))
    # # import wmi
    # #
    # # Pc = wmi.WMI()
    # # os_info = Pc.Win32_OperatingSystem()[0]
    # # os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    # #
    # # print(f'操作系统: {os_name.decode()}')
    # import json
    #
    # with open(r"C:\Users\RAYDATA\Desktop\test.json", "r") as f:
    #     data = f.read()
    #     for item in eval(data):
    #         item["count"] = int(item["count"])
    #         print(item)
