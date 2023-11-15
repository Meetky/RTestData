# -*- coding: utf-8 -*-
# @Project  :MyProject
# @File     :views.py
# @Date     :2021/4/28 11:28
# @Author   :Concon
# @Email    :kangkang.liu@raykite.com
# @Software :PyCharm
import json
from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from my_api.demo.create_area import GenerationArea
from my_api.demo.create_bj import GenerationBJ
from my_api.demo.create_3d_data import Generation3DData
from my_api.demo.create_drawpath import CreateDrawPath
from my_api.demo.create_flyline import CreateFlyLine
from my_api.demo.form import GenerationForm
from my_api.demo.get_2d_resource import Resource_2D
from my_api.demo.timer_shaft import GenerationTimerShaft


@csrf_exempt
def tabulation(request):
    with open(r'./my_api/datas/tabulation.json', encoding="utf-8") as f:
        # dic = json.load(f)
        data = f.read()
    if request.method == 'GET':
        # return HttpResponse(json.dumps(dic))
        return HttpResponse(data)
    # else:
    #     dic['msg'] = '方法错误'
    #     return HttpResponse(json.dumps(dic, ensure_ascii=False))


@csrf_exempt
def form(request):
    # with open(r'./my_api/datas/tabulation.json', encoding="utf-8") as f:
    #     dic = json.load(f)
    # if request.method == 'GET':
    #     return HttpResponse(json.dumps(dic))
    # else:
    #     dic['msg'] = '方法错误'
    #     return HttpResponse(json.dumps(dic, ensure_ascii=False))
    form_ = GenerationForm()
    if request.method == 'GET' or request.method == 'POST':
        try:
            a = int(request.GET.get('a'))
            if a == 0:
                raise ValueError
            form_.main(a)
            return HttpResponse(json.dumps(form_.page_data))
        except:
            form_.main(random.randint(1, 50))
            return HttpResponse(json.dumps(form_.page_data))
    else:
        form_.page_data['code'] = '10000'
        form_.page_data["msg"] = "方法错误"
        return HttpResponse(json.dumps(form_.page_data, ensure_ascii=False))


@csrf_exempt
def form_user(request):
    # with open(r'./my_api/datas/tabulation.json', encoding="utf-8") as f:
    #     dic = json.load(f)
    # if request.method == 'GET':
    #     return HttpResponse(json.dumps(dic))
    # else:
    #     dic['msg'] = '方法错误'
    #     return HttpResponse(json.dumps(dic, ensure_ascii=False))
    form_ = GenerationForm()
    if request.method == 'GET' or request.method == 'POST':
        try:
            a = int(request.GET.get('a'))
            if a == 0:
                raise ValueError
            form_.main_user(a)
            return HttpResponse(json.dumps(form_.page_data))
        except:
            form_.main_user(random.randint(1, 50))
            return HttpResponse(json.dumps(form_.page_data))
    else:
        form_.page_data['code'] = '10000'
        form_.page_data["msg"] = "方法错误"
        return HttpResponse(json.dumps(form_.page_data, ensure_ascii=False))


# @csrf_exempt
# def area(request):
#     """
#         圆形区域临时数据
#     """
#     with open(r'./my_api/datas/circular_region.json', encoding="utf-8") as f:
#         dic = json.load(f)
#     if request.method == 'GET':
#         return HttpResponse(json.dumps(dic))
#     else:
#         dic['code'] = '10000'
#         dic['msg'] = '方法错误'
#         return HttpResponse(json.dumps(dic, ensure_ascii=False))

@csrf_exempt
def get_token(request):
    result = {"token": ""}
    token = "token获取异常，请重试"
    if len(request.path_info) >= 800:
        result["token"] = request.path_info.split("/")[-1]
        return HttpResponse(json.dumps(result))
    if request.method == "GET":
        token = request.GET.get("token", default="token获取异常，请重试")
    elif request.method == "POST":
        if "application/json" in request.headers["content-Type"]:
            print("body:>>>>>", request.body.decode(), "<<<<<")
            token = json.loads(request.body.decode())["token"]
        elif "application/x-www-form-urlencoded" in request.headers["content-Type"]:
            token = request.POST.get("token", "")
    result["token"] = token
    return HttpResponse(json.dumps(result))


@csrf_exempt
def get_data(request):
    data = {}
    if request.method == "GET":
        if bool(request.GET):
            for key in request.GET.keys():
                data[key] = request.GET[key]
        else:
            data["data"] = request.path_info.split("/")[-1]
        return HttpResponse(json.dumps(data))
    elif request.method == "POST":
        return HttpResponse(request.body)


@csrf_exempt
def random_number(request):
    return HttpResponse(json.dumps({
        "data": random.randint(0, 100)
    }))


def eq(request):
    try:
        url_parse = int(request.path_info[1:-1].split("g")[-1])
        print(url_parse)
        if url_parse == 2:
            return render(request, 'kangkang2.html')
        elif url_parse == 3:
            return render(request, 'kangkang3.html')
        elif url_parse == 0:
            return render(request, 'receipt.html')
        else:
            return render(request, 'kangkang1.html')
    except:
        return render(request, 'kangkang1.html')


# 装饰器
def f(a, b, c):
    def deco(func):
        def wrapper(*args, **kwargs):
            instance = args[0]
            if instance.method == 'GET':
                try:
                    a = int(instance.GET.get('a'))
                    if a == 0:
                        raise ValueError
                    args[1].main(a)
                    return HttpResponse(json.dumps(args[1].page_data))
                except:
                    args[1].main(random.randint(1, 50))
                    return HttpResponse(json.dumps(args[1].page_data))
            else:
                args[1].page_data["msg"] = "方法错误"
                args[1].page_data["code"] = "10000"
                return HttpResponse(json.dumps(args[1].page_data, ensure_ascii=False))

        return wrapper

    return deco


@csrf_exempt
def get_2d_resource(request):
    """
        文本、图片、视频、视频流
    """
    get_2d = Resource_2D()
    if request.method == 'GET':
        get_2d.main()
        return HttpResponse(json.dumps(get_2d.page_data))
    else:
        get_2d.page_data['code'] = '10000'
        get_2d.page_data["msg"] = "方法错误"
        return HttpResponse(json.dumps(get_2d.page_data, ensure_ascii=False))


@csrf_exempt
def sign_data(request):
    """
        自由标记
    """
    gen = GenerationBJ()
    if request.method == 'GET' or request.method == 'POST':
        try:
            a = int(request.GET.get('a'))
            if a == 0:
                raise ValueError
            gen.main(a)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            gen.main(random.randint(1, 50))
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data['code'] = '10000'
        gen.page_data["msg"] = "方法错误"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


@csrf_exempt
def sign1_data(request):
    """
        自由标记
    """
    gen = GenerationBJ()
    if request.method == 'GET' or request.method == 'POST':
        try:
            a = int(request.GET.get('a'))
            if a == 0:
                raise ValueError
            gen.main1(a)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            gen.main1(random.randint(1, 50))
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data['code'] = '10000'
        gen.page_data["msg"] = "方法错误"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


def fly_line(request):
    """
        飞线
    """
    gen = CreateFlyLine()
    if request.method == 'GET' or request.method == 'POST':
        try:
            a = int(request.GET.get('a'))
            if a == 0:
                raise ValueError
            gen.main(a)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            a = random.randint(1, 50)
            gen.main(a)
            print("数量:", a)
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data['code'] = '10000'
        gen.page_data["msg"] = "方法错误"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


def draw_path(request):
    """
        路径
    """
    gen = CreateDrawPath()
    if request.method == 'GET':
        try:

            if request.GET.get('a') and request.GET.get('node'):
                a = int(request.GET.get('a'))
                node = int(request.GET.get('node'))
                gen.main(node, a)
                if node == 0:
                    raise ValueError
            elif request.GET.get('a') and not request.GET.get('node'):
                a = int(request.GET.get('a'))
                gen.main(num=a)
            elif not request.GET.get('a') and request.GET.get('node'):
                node = int(request.GET.get('node'))
                gen.main(node=node)
            else:
                raise ValueError
            return HttpResponse(json.dumps(gen.page_data))
        except:
            node = random.randint(1, 5)
            gen.main(node=node)
            # print("节点数量:", node)
            return HttpResponse(json.dumps(gen.page_data))

    else:
        gen.page_data['code'] = '10000'
        gen.page_data["msg"] = "方法错误"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


@csrf_exempt
def round_area(request):
    """
            圆形区域数据
        """
    gen = GenerationArea()
    if request.method == 'GET':
        try:
            a = int(request.GET.get('a'))
            if a == 0:
                raise ValueError
            gen.round_area(a)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            gen.round_area(random.randint(1, 50))
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data["msg"] = "方法错误"
        gen.page_data["code"] = "10000"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


# rec_area
@csrf_exempt
def rec_area(request):
    """
        矩形区域数据
    """
    gen = GenerationArea()
    if request.method == 'GET':
        try:
            a = int(request.GET.get('a'))
            if a == 0:
                raise ValueError
            gen.rec_area(a)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            gen.rec_area(random.randint(1, 50))
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data["msg"] = "方法错误"
        gen.page_data["code"] = "10000"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


# polygon_area
@csrf_exempt
def polygon_area(request):
    """
        矩形区域数据
    """
    gen = GenerationArea()
    if request.method == 'GET':
        try:
            a = int(request.GET.get('a'))
            if a == 0:
                raise ValueError
            gen.polygon_area(a)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            gen.polygon_area(random.randint(1, 10))
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data["msg"] = "方法错误"
        gen.page_data["code"] = "10000"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


@csrf_exempt
def particle(request):
    """
        粒子图
    """
    gen = Generation3DData()
    if request.method == 'GET' or request.method == 'POST':
        try:
            a = int(request.GET.get('a'))
            if a < 3:
                raise ValueError
            gen.particle(a)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            gen.particle(random.randint(100, 1000))
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data["msg"] = "方法错误"
        gen.page_data["code"] = "10000"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


def trajectory(request):
    """
        轨迹
    """
    gen = Generation3DData()
    if request.method == 'GET' or request.method == 'POST':
        try:
            a = int(request.GET.get('a'))
            if a < 1:
                raise ValueError
            gen.trajectory(a)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            gen.trajectory(random.randint(100, 1000))
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data["msg"] = "方法错误"
        gen.page_data["code"] = "10000"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


@csrf_exempt
def hot_chart(request):
    """
        热力图
    """
    gen = Generation3DData()
    if request.method == 'GET' or request.method == 'POST':
        try:
            a = int(request.GET.get('a'))
            c = str(request.GET.get('c'))
            print(f"C is {c}")
            if a < 3:
                raise ValueError
            gen.hot_chart(a)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            gen.hot_chart(random.randint(100, 1000))
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data["msg"] = "方法错误"
        gen.page_data["code"] = "10000"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))


@csrf_exempt
def timer_shaft(request):
    """
        时间轴
    """
    gen = GenerationTimerShaft()
    if request.method == 'GET' or request.method == 'POST':
        try:
            node = int(request.GET.get('node'))
            tag = int(request.GET.get('tag'))

            gen.main(node, tag)
            return HttpResponse(json.dumps(gen.page_data))
        except:
            gen.main(5, 2)
            return HttpResponse(json.dumps(gen.page_data))
    else:
        gen.page_data["msg"] = "方法错误"
        return HttpResponse(json.dumps(gen.page_data, ensure_ascii=False))
