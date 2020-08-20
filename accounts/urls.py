
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from accounts.views import register,addid
from accounts.views import login,mesg,cmptTask,profile,question,userData,dashboard,task,adminlogin,admindashboard,submit,logout,adminprofile,detail,delete,userprofile,recievetask,deletetask
from main.views import assign,editask,create,SubmitTask,showprogress,click


urlpatterns = [
    path("register", register, name = "register"),
    path("login",login, name="login"),
    path("mail",mesg, name='message'),
    path("dashboard",dashboard, name='dashboard'),
    path("profile/userData",userData, name='userData'),
    path("questions",question, name='questions'),
    path("profile/edit" , profile , name='edit'),
    path("profile/task",task,name='task'),
    path("adminlogin", adminlogin , name='adminlogin'),
    path("admindashboard", admindashboard,name = 'admindashboard'),
    path("profile/task/submit",submit, name= 'submit' ),
    path("profile/task/update/<int:id>/", showprogress, name='percent'),
    path("profile/task/assign/<int:id>",assign, name= 'assign' ),
    path("logout",logout,name='logout'),
    path("admindashboard/userdata",userData,name='admindata'),
    path("admindashboard/edit",adminprofile,name='adminedit'),
   # path("admindashboard/detail",detail,name='detail'),
    path("admindashboard/delete/<int:id>/",delete,name = 'delete'),
    path("admindashboard/update/<int:id>/",editask,name='update'),
   # path("admindashboard/up/<int:id>/",editask,name='update'),
    path("admindashboard/createTask",create,name = 'create'),
    path("admindashboard/userprofile/<int:id>/", userprofile, name='userprofile'),
    path("profile/task/submitTask/<int:id>/",SubmitTask,name='submitTask'),
    path("admindashboard/checkCompleteTasks",recievetask,name = 'complete'),
    path("admindashboard/checkCompleteTasks/<int:id>",deletetask,name ='deletetask'),
    path("admindashbaord/addID",addid,name = 'AddID'),
    path("admindashbaord/Completed-Task/<int:id>/",cmptTask,name='completedTask'),
    path("accounts/click/<int:id>/", click, name='click')


   # url(r'^(?P<slug>[-\W])/$',profile , name ='profile')

    #FOR PASSWORD RESET

    #path("password_reset", password_rest, name = 'password_reset")
    #path("/password_reset",auth_views.PasswordResetView,name = 'PasswordResetView')
    #path("contact",mesg, name= 'contact'),
    #path("profile/edit",editProfile, name='edit'),
]