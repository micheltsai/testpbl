from django.shortcuts import render
from . import form
# Create your views here.
from login import models
from django.shortcuts import redirect

# Create your views here.
from .models import Group


def index(request):
    test_class = models.CreateClass.objects.all()
    context = {'create_class': test_class}
    return render(request, 'index.html', context)


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('index')
    if request.method == 'POST':
        login_form = form.UserForm(request.POST)
        message = '請檢查內容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            identify = login_form.cleaned_data.get('identify')
            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用戶不存在！'
                return render(request, 'login_base.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['user_identify'] = user.identify
                return redirect('index')
            else:
                message = '密碼不正確！'
                return render(request, 'login_base.html', locals())
        else:
            return render(request, 'login_base.html', locals())

    login_form = form.UserForm()
    return render(request, 'login_base.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = form.RegisterForm(request.POST)
        message = "請檢查填寫內容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            identify = register_form.cleaned_data.get('identify')
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'register_base.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'register_base.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'email已存在！'
                    return render(request, 'register_base.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.identify = identify
                new_user.save()

                return redirect('login')
        else:
            return render(request, 'register_base.html', locals())
    register_form = form.RegisterForm()
    return render(request, 'register_base.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('index')
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("index")


def create_class(request):
    # if request.session['user_identify'] == 'teacher':
        if request.method == 'POST':
            class_form = form.ClassForm(request.POST)
            if class_form.is_valid():
                class_form.save()
                return redirect('index')
        else:
            class_form = form.ClassForm()
        context = {
            'class_form': class_form,
        }
        return render(request, 'create_class.html', context)


def create_activate(request):
    class_c = models.CreateClass.objects.all()
    if request.method == 'POST':
        activate = form.ActivateForm(request.POST)
        if activate.is_valid():
            activate.save()
            return redirect('index')
    else:
        activate = form.ActivateForm()
    context = {
        'class_c': class_c,
        'activate': activate,
    }
    return render(request, 'create_activate.html', context)


def view_activate(request, pk):
    activte_a = models.CreateActivate.objects.filter(class_id=pk)
    context = {
        'activate_a': activte_a,
        'pk': pk
    }
    return render(request, 'view_activate.html', context)


def view_group(request, pk):
    activate_a = models.CreateActivate.objects.filter(id=pk)
    group_a = models.Group.objects.all()
    context = {
        'activate_a': activate_a,
        'group_a': group_a,
        'pk': pk
    }
    return render(request, 'view_group.html', context)


def create_group(request, pk):
    activate_a = models.CreateActivate.objects.filter(id=pk)
    user_a = models.User.objects.all()
    if request.method == 'POST':
        group = form.CreateGroup(request.POST)
        tests = request.POST.getlist('check_box_list')
        if group.is_valid():
            obj : Group()
            obj = group.save()
            for t in tests:
                obj.group_user.add(t)
                obj.save()
            return redirect('index')
    else:
        group = form.CreateGroup()
    context = {
        'user_a': user_a,
        'activate_a': activate_a,
        'group': group
    }
    return render(request, 'create_group.html', context)
