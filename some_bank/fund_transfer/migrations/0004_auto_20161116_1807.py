# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund_transfer', '0003_auto_20161116_0931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeraccount',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='payee',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='customeraccount',
            name='account_type',
            field=models.CharField(choices=[('s', 'Savings'), ('c', 'Current')], default='s', max_length=1),
        ),
        migrations.AlterField(
            model_name='payee',
            name='account_type',
            field=models.CharField(choices=[('s', 'Savings'), ('c', 'Current')], default='s', max_length=1),
        ),
    ]