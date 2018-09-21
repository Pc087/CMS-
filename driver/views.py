from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from .models import Driver, Department
from .forms import DriverEditForm
from complaints.views import get_pages

# Create your views here.

@login_required
def driver_list(request):
    """司机列表"""

    # dpt获取当前用户部门
    dpt = request.user.profile.department.name

    # 构建字典表
    departments = {
        '西蜀': Driver.driver.xishu(),
        '东吴': Driver.driver.dongwu(),
        '北魏': Driver.driver.beiwei(),
    }

    # 判断用户权限等级
    if request.user.is_superuser:
        objects = Driver.driver.all()
    else:
        objects = departments.get(dpt)

    # 分页
    posts = get_pages(request, objects_list=objects)
    return render(request, 'driver_list.html', locals())


@login_required
def driver_detail(request, work_number):
    posts = get_object_or_404(Driver, work_number=work_number)
    if request.method == 'POST':
        form = DriverEditForm(instance=posts, data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'result': 'OK'})

    # 判断能否编辑
    to_edit = 1 if request.GET.get('to_edit', '') else 0
    form = DriverEditForm(instance=posts)
    return render(request, 'driver_detail.html', locals())


@login_required
def driver_del(request):
    work_number = request.GET.get('worknum', '')
    print(work_number)
    Driver.driver.filter(work_number=work_number).delete()
    return redirect(reverse('driver_list'))

def driver_query(key, kw):
    search_dict ={
        'wk': Driver.driver.filter(work_number__contains=kw),
        'xm': Driver.driver.filter(name__contains=kw),
        'cp': Driver.driver.filter(car_number__contains=kw),
        'tel': Driver.driver.filter(tel__contains=kw),
    }
    return search_dict.get(key)

@login_required
def driver_search(request):
    kw = request.GET.get('kw', '')
    num = Driver.driver.filter(name__contains=kw).count()

    # 换条件搜索
    keyword_list = ['wk', 'xm', 'cp', 'tel']
    for keyword in keyword_list:
        if driver_query(keyword, kw).count() >0:
            objects = driver_query(keyword, kw)
            posts = get_pages(request, objects_list=objects)
            break

    return render(request, 'driver_list.html', locals())
