# Generated by Django 2.2.7 on 2019-11-26 00:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191122_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='添加时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='timer',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='添加时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timer',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]
