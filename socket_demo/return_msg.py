import json

from my_api.demo.get_2d_resource import Resource_2D
from my_api.demo.create_bj import GenerationBJ
from my_api.demo.form import GenerationForm
from my_api.demo.create_flyline import CreateFlyLine

resource2d = Resource_2D()
sign = GenerationBJ()
form = GenerationForm()
flyline = CreateFlyLine()


def return_msg(client_msg):
    default = {
        "2d": "返回2d资源内容",
        "表格": "返回表格数据",
        "标记": "返回3d标记数据",
        "飞线": "返回3d飞线数据"
    }
    # if not str(client_msg) or str(client_msg) == "" or str(client_msg) == " ":
    #     return json.dumps(default)
    if str(client_msg) == "2d":
        return json.dumps(resource2d.main())
    elif str(client_msg) == "表格":
        return json.dumps(form.main_user(16))
    elif str(client_msg) == "标记":
        return json.dumps(sign.main(3))
    elif str(client_msg) == "飞线":
        return json.dumps(flyline.main(3))

    return json.dumps(default)


if __name__ == '__main__':
    print(return_msg(" "))
