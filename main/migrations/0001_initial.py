# Generated by Django 2.2.7 on 2020-01-07 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorkType', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=1000)),
                ('message', models.CharField(blank=True, max_length=1000)),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='pics')),
                ('file', models.FileField(upload_to='router_specifications')),
                ('Client_Name', models.CharField(max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Urgent', models.BooleanField(default=False)),
                ('Worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='completeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktype', models.CharField(max_length=1000)),
                ('aboutTask', models.CharField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to='completedPics')),
                ('file', models.FileField(upload_to='completed')),
                ('Client_Name', models.CharField(max_length=100)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
