# Generated by Django 2.2.7 on 2020-01-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_announce'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completetask',
            name='Team_member',
        ),
        migrations.AddField(
            model_name='completetask',
            name='Name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]