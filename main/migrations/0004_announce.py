# Generated by Django 2.2.7 on 2020-01-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200109_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accouncement', models.CharField(max_length=1000)),
            ],
        ),
    ]