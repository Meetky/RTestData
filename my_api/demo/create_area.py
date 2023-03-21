# -*- coding: utf-8 -*-
# @Project  :MyProject
# @File     :create_area
# @Date     :2021/7/14 22:10
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
import copy
import random

from my_api.demo.data_base import DataBase


class GenerationArea(DataBase):
    def __init__(self):
        super().__init__()
        self.round_area_data = {
            "id": "",
            "coordCenter": {
                "lat": 39.91889913158951,
                "lng": 116.27093797257456
            },
            "coordRadius": {
                "lat": 39.900237366749025,
                "lng": 116.28178443752388
            }
        }
        self.rec_area_data = {
            "id": "",
            "coordLeft": {
                "lat": 31.257373168862088,
                "lng": 121.49556195871531
            },
            "coordRight": {
                "lat": 31.260480867166763,
                "lng": 121.49231529958213
            }
        }
        self.polygon_area_data = {
            "id": "",
            "coordshape": []
        }

    def round_area(self, num):
        for n in range(num):
            radii = random.uniform(0.03, 0.07)
            data = copy.deepcopy(self.round_area_data)
            data["id"] = n
            data["coordCenter"]["lat"], \
            data["coordCenter"]["lng"] = self.generation_lat_lng_bj()
            data["coordRadius"]["lat"] = data["coordCenter"]["lat"] + radii
            data["coordRadius"]["lng"] = data["coordCenter"]["lng"] + radii
            self.page_data["data"].append(data)
        self.page_data["total"] = num
        return self.page_data

    def rec_area(self, num):
        for n in range(num):
            radii = random.uniform(0.03, 0.07)
            data = copy.deepcopy(self.rec_area_data)
            data["id"] = n
            data["coordLeft"]["lat"], \
            data["coordLeft"]["lng"] = self.generation_lat_lng_bj()
            data["coordRight"]["lat"] = data["coordLeft"]["lat"] + radii
            data["coordRight"]["lng"] = data["coordLeft"]["lng"] + radii
            self.page_data["data"].append(data)
        self.page_data["total"] = num
        return self.page_data

    def polygon_area(self, num):
        for n in range(num):
            data = copy.deepcopy(self.polygon_area_data)
            data["id"] = n
            lat, lng = self.generation_lat_lng_bj()
            data["coordshape"].append({"lat": lat, "lng": lng})
            for i in range(random.randint(2, 5)):
                data["coordshape"].append(
                    {
                        "lat": lat + random.uniform(0.1, 0.3),
                        "lng": lng + random.uniform(0.1, 0.3)
                    })
            self.page_data["data"].append(data)
        self.page_data["total"] = num
        return self.page_data


if __name__ == '__main__':
    a = GenerationArea()
    print(a.polygon_area(2))
