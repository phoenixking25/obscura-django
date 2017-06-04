# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 11:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obscura', '0002_auto_20170602_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='levelschema',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='levelschema',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='obscura.userSchema'),
        ),
        migrations.AlterField(
            model_name='levelschema',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userschema',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userschema',
            name='phone',
            field=models.IntegerField(help_text='Enter user phone number', null=True),
        ),
    ]
