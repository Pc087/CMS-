# CMS投诉管理系统

## 需求
    由于公司服务投诉热线业务转移出公司，为了方便公司内部人员对投诉文件的处理，避免传统的word文档以QQ方式发送工作而造成文件杂乱。

## 开发环境及框架
- Python 3.6.3
- Django 2.1
- django-simple-captcha

## 功能模块
- 投诉管理
- 驾驶员管理
- 用户账号管理

## 个人遇到的难点
- 综合查询
- 编辑和删除

### 综合查询
由于平时工作中要查询一些历史投诉文件，如果非分为多个不同类型分别查询，这样用起来不方便，在投诉页面只提供了一个搜索框，功能是实现关键词在模型字段逐个匹配，并返回结果；
  

```
@login_required
def complaint_search(request):
    """投诉工单搜索"""
    kw = str(request.GET.get('kw'))
    is_exist = Complaint.objects.filter(complaint_number__contains=kw).count()
    if is_exist == 0:
        is_exist = Complaint.objects.filter(title__contains=kw).count()
        if is_exist == 0:
            objects = Complaint.objects.filter(content__contains=kw)
        else:
            objects = Complaint.objects.filter(title__contains=kw)
    else:
        objects = Complaint.objects.filter(complaint_number__contains=kw)

    paginator = Paginator(objects, 12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', locals())
```

上面是开始的实现方案，虽然功能已经实现，但代码有些重复而且混乱，于是我定义了一个方法，利用字典表返回查询结果，在主函数用列表循环判断查询。

```
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
```

