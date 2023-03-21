# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :MyProject
 @Date     :2022/1/14 18:24
 @File     :create_flyline.py
 @Description: 
 @Software :PyCharm
*****************************
"""
import copy

from my_api.demo.data_base import DataBase


class CreateFlyLine(DataBase):
    def __init__(self):
        super().__init__()
        self.data = {
            "id": "1",
            "cityStart": "北京市",
            "cityEnd": "北京市"
        }

    def main(self, num):
        for n in range(num):
            cityStart, cityEnd = self.generation_fly_line()
            self.data = copy.deepcopy(self.data)
            self.data["id"] = n
            self.data["cityStart"] = cityStart
            self.data["cityEnd"] = cityEnd
            self.page_data["data"].append(self.data)
        self.page_data["total"] = num
        return self.page_data


if __name__ == '__main__':
    g = CreateFlyLine()
    print(g.generation_fly_line())
