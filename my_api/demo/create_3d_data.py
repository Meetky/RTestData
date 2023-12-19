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
            data = copy.deepcopy(self.data)
            data["id"] = n
            data["x"], data["y"], data["z"] = self.generation_x_y_z()
            self.page_data["data"].append(data)
        self.page_data["total"] = num
        return self.page_data

    def pipeline(self):
        data = {}
        # data["PipelineColor"] = "1-0-#000000"
        data["Pipelinethickness"] = random.randint(1, 100)
        data["SweepSwitch"] = random.choice(["on", "off"])
        # data["SweepColor"] = "1-0-#FFF000"
        data["Sweepdirection"] = random.choice(["forward", "backward"])
        data["Sweeprate"] = random.randint(1, 100)
        self.page_data["data"].append(data)
        return self.page_data

    def glb_skeletal_animation(self, num):
        """
        GLB骨骼动画
        """
        for n in range(num):
            data = copy.deepcopy(self.data)
            data["id"] = n
            data["coordinate"]["lat"], data["coordinate"]["lng"] = self.generation_lat_lng_china()
            data["positionX"], data["positionY"], data["positionZ"] = self.generation_glb_x_y_z()
            data["rotationX"] = 0
            data["rotationY"] = 0
            data["rotationZ"] = 0
            data["scaleX"] = 0.09
            data["scaleY"] = 0.09
            data["scaleZ"] = 0.09
            data["children"] = [{
                "id": n,
                "name": "test",
                "rotationX": 0,
                "rotationY": 0,
                "rotationZ": 0,
                "scaleX": 1,
                "scaleY": 1,
                "scaleZ": 1
            }]
            data["children"][0]["positionX"], data["children"][0]["positionY"], data["children"][0]["positionZ"] = self.generation_glb_x_y_z()
            self.page_data["data"].append(data)

        self.page_data["total"] = num
        return self.page_data


if __name__ == '__main__':
    gen = Generation3DData()
    print(gen.glb_skeletal_animation(1))
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
