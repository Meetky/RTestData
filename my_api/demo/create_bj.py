# -*- coding: utf-8 -*-
# @Project  :MyProject
# @File     :create_bj
# @Date     :2021/7/13 13:23
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
import copy
import random

from my_api.demo.data_base import DataBase


class GenerationBJ(DataBase):
    def __init__(self):
        self.data = {
            "unit": "",
            "subTitle": "",
            "id": "a444",
            "title": "崇文区",
            "value": "1062",
            "content": "a内容文本4",
            "imageUrl": "",
            "videoUrl": "",
            "coordinate": {
                "lat": 39.8807,
                "lng": 116.43005
            }
        }
        super().__init__()

    # def generation_lat_lng_bj(self):
    #     """
    #     左上：40.470057,115.91644
    #     左下：39.7375,115.91644
    #     右上：40.470057,116.78933
    #     右下：39.7375,116.78933
    #     """
    #     # (lat,lng)
    #     return random.uniform(39.7375, 40.4700), random.uniform(115.91644, 116.78933)

    def main(self, num):
        for i in range(num):
            # 生成文字

            # 生成单个坐标
            self.data = copy.deepcopy(self.data)
            self.data["unit"] = self.GBK2312(2)
            self.data["id"] = i
            self.data["city"] = self.get_city()
            self.data["value"] = random.randint(100, 999)
            self.data["content"] = self.GBK2312(200)
            self.data["videoUrl"] = self.get_2d_resource()[2]
            self.data["imageUrl"] = self.get_2d_resource()[1]
            self.data["subTitle"], self.data["title"] = self.GBK2312(6), self.GBK2312(6)
            self.data["coordinate"]["lat"], self.data["coordinate"]["lng"] = self.generation_lat_lng_bj()
            # 加入数据
            self.page_data["data"].append(self.data)
        self.page_data["total"] = num
        return self.page_data

    def main1(self, num):
        for i in range(num):
            # 生成文字

            # 生成单个坐标
            self.data = copy.deepcopy(self.data)
            self.data["unit"] = self.GBK2312(2)
            self.data["id"] = i
            self.data["city"] = "北京市"
            self.data["value"] = random.randint(100, 999)
            self.data["content"] = self.GBK2312(200)
            self.data["videoUrl"] = self.get_2d_resource()[2]
            self.data["imageUrl"] = self.get_2d_resource()[1]
            self.data["subTitle"], self.data["title"] = self.GBK2312(6), self.GBK2312(6)
            self.data["coordinate"]["lat"], self.data["coordinate"]["lng"] = (39.73920626339363, 116.44766778161552)
            # 加入数据
            self.page_data["data"].append(self.data)
        self.page_data["total"] = num
        return self.page_data

if __name__ == '__main__':
    g = GenerationBJ()
    print(g.main(5))
