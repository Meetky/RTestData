"""my_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    # 推荐这种方法:url地址这样写/info?p1=123,获取数据用request.GET.get('p1')
    url(r"token/", views.get_token, name="获取token"),
    url(r"data/", views.get_data, name="参数返回"),
    url(r"random", views.random_number, name="随机数0-100"),
    url(r'form/', views.form, name='表格'),
    url(r'formU/', views.form_user, name='表格_用户信息'),
    url(r'tabulation/', views.tabulation, name='表格默认数据'),
    url(r'kangkang[0-9]/', views.eq, name='均衡器iframe'),
    url(r'kangkang/', views.eq, name='均衡器iframe'),
    # url(r'area/', views.area, name='area'), 弃用
    url(r'sign/', views.sign_data, name="标记"),
    url(r'sign1/', views.sign1_data, name="标记"),
    url(r'fline', views.fly_line, name="飞线"),
    url(r'drawPath', views.draw_path, name="路径绘制"),
    url(r'round_area', views.round_area, name="原型区域"),
    url(r'rec_area', views.rec_area, name="矩形区域"),
    url(r'polygon_area', views.polygon_area, "多边形区域"),
    url(r'particle', views.particle, name="粒子图"),
    url(r'hot', views.hot_chart, name="热区"),
    url(r'trajectory', views.trajectory, name="轨迹"),
    url(r'pipeline', views.pipeline_data, name="管线"),
    url(r'glb', views.glb_skeletal_animation_data, name="GLB骨骼动画"),
    url(r'res', views.get_2d_resource, name="2d资源"),
    url(r'timer', views.timer_shaft, name="时间轴"),
]
