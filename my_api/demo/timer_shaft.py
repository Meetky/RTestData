# -*- coding: utf-8 -*-
# @Project  :MyProject
# @File     :timer_shaft
# @Description: 
# @Date     :2021/8/26 13:17
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
import random

from my_api.demo.data_base import DataBase


class GenerationTimerShaft(DataBase):
    def __init__(self):
        super().__init__()
        self.data = []

    def main(self, node: int, tag: int):
        node_time = 1990
        for n in range(1, node + 1):
            tag_ = self.tag(tag)
            tag_[1]["text"] = str(node_time) + "年"
            self.data.append(tag_)
            node_time += 1
        self.page_data["data"] = self.data
        self.page_data["total"] = node
        return self.page_data

    def tag(self, tag: int):
        return [{"text": self.GBK2312(random.randint(3, 6))} for t in range(1, tag + 1)]


if __name__ == '__main__':
    ts = GenerationTimerShaft()
    print(ts.main(5, 2))
