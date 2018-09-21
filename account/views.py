from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm, ProfileRegistrationForm
from .models import Profile
from driver.models import Department
from complaints.views import get_pages

# Create your views here.


class UserLoginView(View):
    """
    用户登录界面
    """

    def get(self, request):
        forms = LoginForm()
        return render(request, 'login.html', locals())

    def post(self, request):
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(username=username, password=pwd)
            if user:
                login(request, user)
                data = {'result': 'OK'}
                return JsonResponse(data)
            else:
                return JsonResponse({'result': '用户或密码错误'})
        else:
            return JsonResponse({'result': '验证码错误'})


def user_logout(request):
    logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)


def account_list(request):
    objects_list = Profile.objects.all()
    posts = get_pages(request, objects_list=objects_list)
    return render(request, 'account_list.html', locals())


@login_required
def account_add(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        user = request.POST.get('username')
        department = request.POST.get('department')
        if form.is_valid():
            try:
                u = form.save(commit=False)
                u.set_password(form.cleaned_data['password'])
                u.save()
                p = Profile()
                p.department = Department.objects.get(id=int(department))
                p.user = User.objects.get(username=user)
                # 编辑权限
                p.cpt_add = True if request.POST.get('cpt_add') == 'on' else False
                p.cpt_edit = True if request.POST.get('cpt_edit') == 'on' else False
                p.cpt_delete = True if request.POST.get('cpt_delete') == 'on' else False
                p.driver_add = True if request.POST.get('driver_add') == 'on' else False
                p.driver_edit = True if request.POST.get('driver_edit') == 'on' else False
                p.driver_delete = True if request.POST.get('driver_delete') == 'on' else False
                p.save()
                return redirect(reverse('account_list'))
            except Exception as e:
                return messages.error(request, e)

    title = '新增用户'
    form = UserRegistrationForm()
    profile_form = ProfileRegistrationForm()
    return render(request, 'profile_add.html', locals())


@login_required
def account_delete(request):
    rowid = request.GET.get('id', '')
    user_id = Profile.objects.filter(id=rowid).first().user_id
    User.objects.filter(id=user_id).delete()
    return redirect(reverse('account_list'))

@login_required
def account_detail(request, rowid):
    posts = get_object_or_404(Profile, id=rowid)
    if request.method == 'POST':
        form = ProfileRegistrationForm(instance=posts, data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'result':'OK'})

    form = ProfileRegistrationForm(instance=posts)
    return render(request, 'profile_edit.html', locals())

