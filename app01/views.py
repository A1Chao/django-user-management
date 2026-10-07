from django.shortcuts import render, HttpResponse, redirect

from app01.models import Department, UserInfo


def index(request):
    return HttpResponse('欢迎使用')
# Create your views here.

def user_list(request):
    return render(request, 'user_list.html')

def user_add(request):
    return HttpResponse('添加用户')


def weather(request):
    import requests
    res = requests.get(url='https://api.open-meteo.com/v1/forecast?latitude=30.67&longitude=104.07&current=temperature_2m')
    data_list = res.json()
    print(data_list)
    return render(request,'weather.html',{"weather_list":data_list})


def something(request):

    print(request.method)

    print(request.GET)

    print(request.POST)


    return redirect("https://www.baidu.com")


def tpl(request): # 1个用法
    name = "24071120521-晁继捷"
    roles = ["管理员", "CEO", "保安"]
    user_info = {"name": "郭智", "salary": 100000, 'role': "CTO"}

    data_list = [
        {"name": "郭智", "salary": 100000, 'role': "CTO"},
        {"name": "卢慧", "salary": 100000, 'role': "CTO"},
        {"name": "赵建先", "salary": 100000, 'role': "CTO"},
    ]
    return render(request,'tpl.html', {"n1": name, "n2": roles, 'n3': user_info, "n4": data_list})


from django.shortcuts import render, HttpResponse, redirect


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是POST请求，获取用户提交的数据
    # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == "123":
        # return HttpResponse("登录成功")
        return redirect("http://www.chinaunicom.com.cn/")

    # return HttpResponse("登录失败")
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})


def orm(request):
    # #### 1.新建 ####
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="运营部")
    # UserInfo.objects.create(name="武沛齐", password="123", age=19)
    # UserInfo.objects.create(name="朱虎飞", password="666", age=29)
    # UserInfo.objects.create(name="吴阳军", password="666")

    # #### 2.删除 ####
    # UserInfo.objects.filter(id=3).delete()
    # Department.objects.all().delete()
    # #### 3.获取数据 ####
    # 3.1 获取符合条件的所有数据
    # data_list = [对象,对象,对象]  QuerySet类型
    # data_list = UserInfo.objects.all()
    # print(data_list)
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)
    # data_list = [对象,]
    # data_list = UserInfo.objects.filter(id=1)

    # 3.1 获取第一条数据【对象】
    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)
    # #### 4.更新数据 ####
    # UserInfo.objects.all().update(password=9999)
    # UserInfo.objects.filter(id=2).update(age=9999)
    # UserInfo.objects.filter(name="朱虎飞").update(age=9999)
    return HttpResponse("更新成功")


def info_list(request):
    data_list = UserInfo.objects.all()
    return render(request,"info_list.html",{"data_list":data_list})


def info_add(request):
    if request.method == "GET":
        return render(request,'info_add.html')
    user = request.POST.get("user")
    password = request.POST.get("pwd")
    age = request.POST.get("age")

    # 模型字段是 name / password / age，不是 user / pwd
    UserInfo.objects.create(name=user, password=password, age=age or 999)

    return redirect("/info/list/")


def info_delete(request):
    # 列表页的“删除”是 POST 表单；同时兼容 ?nid=<id> 的 GET 写法
    nid = request.POST.get("nid") or request.GET.get("nid")
    if nid:
        UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")
