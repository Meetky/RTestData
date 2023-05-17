# -*- coding: utf-8 -*-
# @Project  :MyProject
# @File     :data_base
# @Date     :2021/7/23 10:41
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
import copy
import random
import os
from faker import Faker
import requests

import yaml

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)


class DataBase:
    def __init__(self):
        self.fake = Faker(locale="zh-CN")
        self.page_data = {
            "code": "0",
            "msg": "OK",
            "total": None,
            "data": []
        }
        self.title = ""

    def get_city(self):
        all_city = [
            '河北省', '山西省', '辽宁省',
            '吉林省', '黑龙江省', '江苏省',
            '浙江省', '安徽省', '福建省',
            '江西省', '山东省', '河南省',
            '湖北省', '湖南省', '广东省',
            '海南省', '四川省', '贵州省',
            '云南省', '陕西省', '甘肃省',
            '青海省', '台湾省',
            '内蒙古自治区', '广西壮族自治区',
            '西藏自治区', '宁夏回族自治区',
            '新疆维吾尔自治区', '北京市',
            '天津市', '上海市', '重庆市',
            '香港特别行政区', '澳门特别行政区'
        ]
        return random.choice(all_city)

    def generation_lat_lng_bj(self):
        """
        左上：40.470057,115.91644              31.763927,118.895972
        左下：39.7375,115.91644                31.490545,118.895972
        右上：40.470057,116.78933              31.763927,119.062588
        右下：39.7375,116.78933                31.490545,119.062588
        """
        # (lat,lng)
        # 北京市
        return random.uniform(39.7375, 40.4700), random.uniform(115.91644, 116.78933)
        # 南京市溧水区
        # return random.uniform(31.490545, 31.763927), random.uniform(118.895972, 119.062588)

    def generation_fly_line(self):
        """板块飞线数据"""
        cityStart = self.get_city()
        cityEnd = self.get_city()
        i = 0
        while i <= 10:
            if i == 10:
                return "获取数据失败，请查看数据源是否正常！"
            if cityEnd != cityStart:
                return cityStart, cityEnd
            cityEnd = self.get_city()
            i += 1

    def generation_draw_path(self, node: int):
        city_list = []
        coordinates_list = []
        n = 1
        while n <= node:
            city = self.get_city()
            lat, lng = self.generation_lat_lng_bj()
            if city not in city_list:
                city_list.append(city)
                coordinates_list.append({
                    "lat": lat,
                    "lng": lng
                })
                n += 1
        return city_list, coordinates_list

    def GBK2312(self, num):
        title = copy.copy(self.title)
        for i in range(num):
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
            val = f'{head:x}{body:x}'
            title += bytes.fromhex(val).decode('gb2312')
        return title

    def get_2d_resource(self):
        page_list = [30, 60, 90, 120, 150, 180, 210, 240]
        imgUrls = requests.get(f"https://image.so.com/zjl?sn={str(random.choice(page_list))}&ch=copyright").json()["list"]
        with open(os.path.join(BASE_PATH, r"datas/resource.yml")) as f:
            data = yaml.safe_load(f)
            text = random.choice(data['text'])
            imgUrl = random.choice(imgUrls)["imgurl"]
            video = random.choice(data['videoURL'])
            vFlowing = random.choice(data['videoFlowing'])
            return text, imgUrl, video, vFlowing

    def generate_personal_information(self):

        # Generate data
        one_data = {
            "name": self.fake.name(),
            "address": self.fake.address(),
            "email": self.fake.email(),
            "date": self.fake.date(),
            "country": self.fake.country(),
            "phone_number": self.fake.phone_number(),
        }
        return one_data


if __name__ == '__main__':
    db = DataBase()
    # print(db.generate_personal_information())
    print(db.get_2d_resource())
