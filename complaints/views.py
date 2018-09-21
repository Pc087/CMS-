from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator, InvalidPage
from .models import Complaint
from driver.models import Driver
from .forms import ComplaintForm
import time

# Create your views here.

@login_required
def complaint_list(request):
    username = request.user.username
    title = "投诉列表"   # 前台标题、标签激活
    if request.user.is_superuser:
        objects = Complaint.objects.this_year().nofinished().all()
    else:
        objects = Complaint.objects.this_year().filter(user__username=username).nofinished().all()

    posts = get_pages(request, objects_list=objects)
    return render(request, 'index.html', locals())

@login_required
def history(request):
    username = request.user.username
    title = "历史投诉"
    if request.user.is_superuser:
        objects = Complaint.objects.order_by('-record_date').all()
    else:
        objects = Complaint.objects.filter(user__username=username).order_by('-record_date').all()

    posts = get_pages(request, objects_list=objects)
    return render(request, 'index.html', locals())


@login_required
def complaint_detail(request, number):
    title = '投诉编辑'

    posts = get_object_or_404(Complaint, complaint_number=number)
    if request.method == 'POST':
        result_form = ComplaintForm(instance=posts, data=request.POST)
        print(result_form)
        if result_form.is_valid():
            result_form.save()
            # return redirect(settings.LOGIN_REDIRECT_URL)
            return JsonResponse({'result': 'ok'})

    to_edit = 1 if request.GET.get('to_edit', '') else 0
    form = ComplaintForm(instance=posts)
    return render(request, 'complaint_detail.html', locals())


class AddView(LoginRequiredMixin, View):
    form_class = ComplaintForm
    template_name = 'complaint_add.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'result': 'ok'})

def complaint_delete(request):
    rowid = request.GET.get('id')
    Complaint.objects.filter(complaint_number=rowid).delete()
    return JsonResponse({'result':'ok'})

@login_required
def driver_search(request):
    """前台ajax请求司机资料"""
    cat = request.GET.get('cat', '')
    results = Driver.driver.filter(work_number=str(cat)).first()
    if results:
        results.__delattr__('_state')
        data = results.__dict__
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'name': '', 'tel': ''}, safe=False)

def get_pages(request, objects_list):
    """
    分页方法get_pages
    """
    paginator = Paginator(objects_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        posts = paginator.page(1)
    return posts


def query(item, kw):
    """自定义搜索"""
    search_dict = {
        'gd': Complaint.objects.filter(complaint_number__contains=kw),
        'bt': Complaint.objects.filter(title__contains=kw),
        'wk': Complaint.objects.filter(driver_work_number__contains=kw),
        'xm': Complaint.objects.filter(driver_name__contains=kw),
        'cp': Complaint.objects.filter(content__contains=kw),
        'nr': Complaint.objects.filter(content__contains=kw),
    }
    return search_dict[item]

@login_required
def all_search(request):
    """搜索框"""

    # 地址栏标签列表
    keyword_list = ['gd', 'bt', 'xm', 'wk', 'cp', 'nr', 'kw']
    title = '投诉搜索列表'

    # 循环
    for keyword in keyword_list:
        # 顶部综合搜索栏
        if keyword == 'kw':
            kw_1 = request.GET.get('kw', '')
            for item in keyword_list:
                # 当count>0获取结果，跳出循环
                if query(item, kw_1).count() >0:
                    objects = query(item=item, kw=kw_1)
                    posts = get_pages(request, objects_list=objects)
                    break

        # 侧边栏搜索框
        else:
            kw = request.GET.get(keyword, '')
            if kw:
                objects = query(item=keyword, kw=kw)
                posts = get_pages(request, objects_list=objects)
                break

    return render(request, 'index.html', locals())
