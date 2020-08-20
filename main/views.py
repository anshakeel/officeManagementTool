from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .forms import assignForm,Edit,createform,returntask,percent,MakeAnnouncement
from .models import worker,completeTask
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.


def showprogress(request, id):
    task = get_object_or_404(worker, id=id)
    if request.method == 'POST':
        form = percent(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    form = percent(instance=task)
    return render(request, 'showprogress.html', {'form': form})
def create(request):
    if request.method == 'POST':
        worktype = request.POST['worktype']
        client = request.POST['client_name']
        file = request.FILES.get('file')
        img = request.FILES.get('image')
        user = request.POST['user']
        dscp = request.POST['description']
        price = request.POST['price']
        urgent = request.POST['urgent']
        print(user)
        x = User.objects.get(id=user)
        print(x)
        if urgent == 'on':
            urgent = True
        else:
            urgent = False
   # form = createform(request.POST or None , request.FILES or None)
   # if form.is_valid():
   #     instance = form.save(commit=False)
   #     instance.save()
   #     messages.success(request,"Successfully Created")
   #     return redirect('admindashboard')
   # context = {
   #     'form' : form
   # }
        worker.objects.create(Worker=x,WorkType=worktype,Client_Name=client
                              ,file=file,image=img,Description=dscp,price=price,Urgent=urgent
                              )

        return redirect('admindashboard')
    u = User.objects.filter(is_staff=False)
    return render(request, 'CreateTask.html', {'u': u})


def home (request):
        return  render(request, "index.html")
def assign(request , id ):
        wor = worker.objects.get(id=id)
        form = assignForm(instance=wor)
        if request.method == 'POST':
          form= assignForm(request.POST , instance= wor)
          if form.is_valid():
                  to = form.cleaned_data['Worker']
                  cm = form.cleaned_data['comment']
                  form.save()
                  messages.info(request, "Task is assisgned to user" + to + "with Comment: "+ cm)
                  mess = form.cleaned_data['Worker']
                  comm = form.cleaned_data['comment']
                  send_mail(
                      'This Task has been assigned to other user',
                      'Testing',
                      settings.EMAIL_HOST_USER,
                      ['ashakeel1219@gmail.com'],
                      fail_silently=False
                  )
                  return redirect('task')
        context = {
                  'form' : form
          }
        return render(request, 'assign.html', context)

def editask(request, id):
    task = get_object_or_404(worker, id= id)
    if request.method == 'POST':
        form = Edit(request.POST,request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('admindashboard')

    form =Edit(instance=task)
    return render(request,'update.html',{'form' : form})

def click(request,id):
    return render(request,'SubmitTask.html', {'id' : id})

def SubmitTask(request,id):
    if request.method == 'POST':
        client = request.POST['client_name1']
        file = request.FILES.get('file1')
        img = request.FILES.get('image1')
        dscp = request.POST['description1']
        # if dscp is None:
        #     dscp = 'just do it'
        # if client is None:
        #     client = 'test'
        x = get_object_or_404(worker, pk=id)
        ins =completeTask.objects.create(Client_Name=client,file=file,image=img,aboutTask=dscp,task=x)
        x.status=True
        x.save()
        return redirect('task')
    return render(request, 'SubmitTask.html', {'id': id})
    # form = returntask(request.POST or None, request.FILES or None)
    # if form.is_valid():

    #     form.task = x
    #     form.save()
    #     x.status= True
    #     x.save()
    #     messages.success(request, "Successfully submitted")
    #     return redirect('task')
    # context = {
    #     'form': form,
    # }

