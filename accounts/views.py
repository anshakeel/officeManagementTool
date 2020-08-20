from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import auth, User
from  django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from main.models import worker,completeTask
from .models import Profile,officeId
from .forms import  UserUpdateForm , ProfileUpdateForm,addID
@login_required(login_url='accounts/adminlogin')
def addid(request):
    form = addID(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Added")
        return redirect('admindashboard')
    context = {
        'form': form
    }
    return render(request, 'addID.html', context)
def deletetask(request, id):
    w = completeTask.objects.get(id = id)
    w.delete()
    return redirect('complete')
def recievetask(request):
    task1 = completeTask.objects.all()
    return render(request,'completed_task.html',{'task1' : task1})

def cmptTask(request,id):

    ss = get_object_or_404(worker,pk=id)
    print(ss)
    t = completeTask.objects.filter(task=ss)
    print(t)
    return render(request,'completed_task.html',{'task': t})

def delete(request, id):
    w = worker.objects.get(id = id)
    w.delete()
    return redirect('admindashboard')
def detail(request):
    us = worker.objects.filter(is_staff=False)
    wo = worker.objects.all()
    pro = Profile.objects.all()
    context = {
        'wo' : wo,
        'pro' : pro
    }
    return render(request,"details.html", context)
@login_required
def adminprofile(request):
    if request.method == 'POST':
         u_form = UserUpdateForm(request.POST , instance=request.user)
         p_form = ProfileUpdateForm(request.POST , request.FILES , instance=request.user.profile)
         if u_form.is_valid() and p_form.is_valid():
             u_form.save()
             p_form.save()
             messages.success(request , f'Your account has been Updated')
             return redirect('admindashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
                   }
    return render(request , 'edit.html' , context)


def logout(request):
    auth.logout(request)
    return redirect('login')
def assign(request):
    return render(request, 'assign.html')
def submit(request):
    return render(request , "submit.html")

def userprofile(request,id):
    prof = Profile.objects.get(id=id)
    user1 = User.objects.get(id=id)
    context = {
        'p': prof,
        'user1': user1
    }
    return render(request,'userprofile.html',context)
#@login_required
def admindashboard(request):
    superusers = User.objects.filter(is_staff=True).count()
    coun = worker.objects.all().count()
    team = User.objects.all().count()
    total = team - superusers
    pro =Profile.objects.all()
    wor = worker.objects.all()
    status = completeTask.objects.filter()
    context = {
        'pro' : pro,
        'wor' : wor,
        'coun' : coun,
        'total': total,
        'super': superusers,

    }

    return render(request,'admindashboard.html',context)
def adminlogin(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password= password)
       if user is not None:
          auth.login(request,user)
          if user.is_staff:
            return redirect("admindashboard")
          else:
              messages.info(request,'You are not authorized to use this login Panel')
              return render(request,'adminlogin.html')
       else:
         messages.info(request,'WRONG CREDENTIALS')
         return redirect('adminlogin')
    else:
     return render(request, 'adminlogin.html')
def task(request):
    wor = worker.objects.filter(Worker=request.user,status=False)
    context = {
        'wor' : wor,
    }
    return render(request, 'DailyTask.html',context)
def dashboard(request):
    return render(request , "profile.html")
def userData(request):
    pro = Profile.objects.all()
    args = {
        'pro' : pro,
        'user1' : request.user,

    }
    return render(request, "userData.html" ,args)

def question(request):
    if request.method == 'POST':
       return render(request, "questions.html")

@login_required
def profile(request):
    if request.method == 'POST':
         u_form = UserUpdateForm(request.POST , instance=request.user)
         p_form = ProfileUpdateForm(request.POST , request.FILES , instance=request.user.profile)
         if u_form.is_valid() and p_form.is_valid():
             u_form.save()
             p_form.save()
             messages.success(request , f'Your account has been Updated')
             return redirect('task')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
                   }
    return render(request , 'edit.html' , context)

def mesg(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail(
            'contact',
            message,
            settings.EMAIL_HOST_USER,
            ['ashakeel1219@gmail.com'],
            fail_silently=False
        )
    return render(request,'mail.html')

def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password= password)
       if user is not None:
           if user.is_staff == False:
              auth.login(request,user)
              return redirect("task")
           else:
               messages.info(request,'You are not authorized to use this Login Panel')
               return redirect('login')
       else:
         messages.info(request,'WRONG CREDENTIALS')
         return redirect('login')
    else:
         return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        officeID = request.POST['officeid']
        if password == password1:
            if User.objects.filter(username=username).exists():
               print('username is taken')
               messages.info(request, 'USERNAME IS TAKEN')
               return redirect('register')
            elif User.objects.filter(email=email).exists():
               print('Email eixsts')
               messages.info(request, 'EMAIL IS TAKEN')
               return redirect('register')
            elif officeId.objects.filter(identification = officeID , username=username).exists() == False:
                messages.info(request, 'Id does not exist')
                return render(request,'register.html')
            else:
                user = User.objects.create_user(username=username,password=password1, email=email,first_name= first_name, last_name= last_name)
                user.save()
                print('User Created')
                messages.info(request, 'Registeration successfull')
                return render(request,'login.html')
        else:
         messages.info(request, 'Passwords not matching')
         return redirect('register')

    else:

        return render(request, 'register.html')

