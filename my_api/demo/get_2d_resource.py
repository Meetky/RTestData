# -*- coding: utf-8 -*-
# @Project  :MyProject
# @File     :video
# @Date     :2021/7/23 10:40
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
from my_api.demo.data_base import DataBase


class Resource_2D(DataBase):
    def __init__(self):
        self.data = {
            "description": ""
        }
        super().__init__()

    def main(self):
        resource = self.get_2d_resource()

        self.data['text'] = self.GBK2312(30)
        self.data['img'] = resource[1]
        self.data['video'] = resource[2]
        self.data['vFolwing'] = resource[3]
        self.page_data["data"].append(self.data)
        return self.page_data
