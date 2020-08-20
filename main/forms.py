from  django.forms import ModelForm
from .models import worker,completeTask,Announce
from  django import forms
from django.forms import models
class assignForm(ModelForm):
     class Meta:
         model = worker
         fields = [
             'Worker',
             'comment',
         ]

class Edit(ModelForm):
    class Meta:
        model = worker
        fields = [
            'Worker',
            'WorkType',
            'Description',
            'Client_Name',
            'image',
            'file',
            'Urgent',
            'message',
        ]

class createform(ModelForm):
    class Meta:
        model = worker
        fields = [
            'Worker',
            'WorkType',
            'Description',
            'Client_Name',
            'image',
            'file',
            'Urgent',
            'price',
            'message',
        ]
        widgets = {
            'Client_Name': forms.TextInput(),
            'WorkType' : forms.TextInput(),
            'Description': forms.TextInput(),
            # 'image': forms.ImageField,
            # 'file': forms.FileField
        }
        labels = {
            'Description' : 'Description Of the Task'
        }


class returntask(ModelForm):
    class Meta:
        model = completeTask
        fields = [
            'task',
            'Client_Name',
            'aboutTask',
            'image',
            'file',
        ]
        widgets = {
            'Client_Name' : forms.TextInput(attrs={'class': 'container'}),
            'aboutTask': forms.Textarea(),
            # 'image': forms.ImageField(),
            # 'file': forms.FileField()
        }

class percent(ModelForm):
    class Meta:
        model = worker
        fields = [
            'progress'
        ]


class MakeAnnouncement(ModelForm):
    class Meta:
        model = Announce
        fields = [
            'accouncement'
        ]