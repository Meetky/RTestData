# -*- coding: utf-8 -*-
"""
*****************************
 @Author   :Concon
 @Email    :meetky@sina.cn
 @Project  :MyProject
 @Date     :2022/5/7 16:29
 @File     :create_drawpath.py
 @Description: 
 @Software :PyCharm
*****************************
"""
import copy

from my_api.demo.data_base import DataBase


class CreateDrawPath(DataBase):
    def __init__(self):
        super().__init__()
        self.data = {
            "id": "1",
            "cityPoints": [],
            "coordinates": []
        }

    def main(self, node=2, num=1):
        for n in range(num):
            city_list, coordinates = self.generation_draw_path(node)
            self.data = copy.deepcopy(self.data)
            self.data["id"] = n
            self.data.update({"cityPoints": city_list})
            self.data.update({"coordinates": coordinates})
            self.page_data["data"].append(self.data)
        self.page_data["total"] = num
        return self.page_data


if __name__ == '__main__':
    dp = CreateDrawPath()
    print(dp.main(num=3))
