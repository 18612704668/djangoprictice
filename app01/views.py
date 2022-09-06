from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")
def user_list(request):
    # 1.优先去项目根目录的templates中寻找【DIRS中配置了OS相关】
    # 2.根据APP的注册顺序，逐一去他们的templates中寻找
    # 3.去APP目录下的templates目录中寻找User_list.html（根据APP的注册顺序，逐一去他们的templates中找）【DIRS中未配置OS相关】
    return render(request,"user_list.html")
def user_add(request):
    return render(request,"user_add.html")
def tpl(request):
    name = "韩超"
    roles = ["管理员","CEO","保安"]
    user_info = {"name":"郭超","salary":"10000","role":"CTO"}
    data_list = [
        {"name": "郭超", "salary": "10000", "role": "CTO"},
        {"name": "卢慧", "salary": "10000", "role": "CTO"},
        {"name": "赵建先", "salary": "10000", "role": "CTO"}
    ]
    return render(request,"tpl.html",{"n1":name,"n2":roles,"n3":user_info,"n4":data_list})