# -*- coding: utf-8 -*-
# @Project  :MyProject
# @File     :form
# @Date     :2021/8/2 15:35
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
import copy
import random

from my_api.demo.data_base import DataBase


class GenerationForm(DataBase):
    def __init__(self):
        super().__init__()
        self.data = {
            "0": {
                "cells": {
                    "0": {
                        "text": "序号"
                    },
                    "1": {
                        "text": "标志"
                    },
                    "2": {
                        "text": "内容"
                    },
                    "3": {
                        "text": "数量"
                    },
                    "4": {
                        "text": "内容"
                    }
                }
            },
            "1": {
                "cells": {
                    "0": {
                        "text": "哈哈哈哈"
                    },
                    "1": {
                        "text": 1
                    },
                    "2": {
                        "text": "大家噶暑假打算结婚股份合计地方都是公开大撒大撒梵蒂冈地方"
                    },
                    "3": {
                        "text": "999"
                    },
                    "4": {
                        "text": "-0.1"
                    }
                }
            }
        }
        self.u_data = {
            "0": {
                "cells": {
                    "0": {
                        "text": "姓名"
                    },
                    "1": {
                        "text": "住址"
                    },
                    "2": {
                        "text": "邮箱"
                    },
                    "3": {
                        "text": "生日"
                    },
                    "4": {
                        "text": "国家"
                    },
                    "5": {
                        "text": "联系方式"
                    }
                }
            },
        }

    def main(self, num):
        data = copy.deepcopy(self.data)
        for n in range(1, num + 1):
            data[str(n)] = self.cells(n)
        self.page_data["data"] = data
        self.page_data["total"] = num
        return self.page_data

    def cells(self, n):
        cells = {
            "cells": {}
        }

        for cell in range(5):
            cells["cells"][str(cell)] = {}
        cells["cells"]['0']['text'] = n
        cells["cells"]['1']['text'] = random.randint(1, 5)
        cells["cells"]['2']['text'] = self.GBK2312(random.randint(1, 300))
        cells["cells"]['3']['text'] = random.randint(1, 9999)
        cells["cells"]['4']['text'] = random.choice([-1, 1])
        return cells

    def cells_user(self):
        cells = {
            "cells": {}
        }
        # 生成用户数据
        u_list = [value for value in self.generate_personal_information().values()]
        # 生成一个用户对象
        for cell in range(6):
            cells["cells"][f"{cell}"] = {"text": u_list[cell]}
        return cells

    def main_user(self, num):
        data = copy.deepcopy(self.u_data)
        for n in range(1, num + 1):
            data[str(n)] = self.cells_user()
        self.page_data["data"] = data
        self.page_data["total"] = num
        return self.page_data


if __name__ == '__main__':
    print("--------test--------")
    g = GenerationForm()
    print(g.main_user(2))
