# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-13 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=25)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
        migrations.CreateModel(
            name='HomeBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=25)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
        migrations.CreateModel(
            name='HomeNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=25)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.CreateModel(
            name='HomeShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=25)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
        migrations.CreateModel(
            name='HomeShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=25)),
                ('trackid', models.CharField(max_length=20)),
                ('categoryid', models.CharField(max_length=25)),
                ('brandname', models.CharField(max_length=25)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=25)),
                ('productid1', models.CharField(max_length=25)),
                ('longname1', models.CharField(max_length=25)),
                ('price1', models.FloatField(default=0)),
                ('marketprice1', models.FloatField(default=0)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=25)),
                ('productid2', models.CharField(max_length=25)),
                ('longname2', models.CharField(max_length=25)),
                ('price2', models.FloatField(default=0)),
                ('marketprice2', models.FloatField(default=0)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=25)),
                ('productid3', models.CharField(max_length=25)),
                ('longname3', models.CharField(max_length=25)),
                ('price3', models.FloatField(default=0)),
                ('marketprice3', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='MainCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_num', models.IntegerField(default=1)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_select', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=25)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=100)),
                ('isxf', models.BooleanField(default=False)),
                ('pmdesc', models.IntegerField(default=0)),
                ('specifics', models.CharField(max_length=50)),
                ('price', models.FloatField(default=1)),
                ('marketprice', models.FloatField(default=1)),
                ('categoryid', models.IntegerField(default=0)),
                ('childcid', models.IntegerField(default=0)),
                ('childcidname', models.CharField(max_length=50)),
                ('dealerid', models.CharField(max_length=50)),
                ('storenums', models.IntegerField(default=1)),
                ('productnum', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='MainMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=20)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='MainOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_num', models.IntegerField(default=0)),
                ('o_status', models.CharField(default=0, max_length=3)),
                ('o_createtiem', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainOrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.MainCart')),
                ('od_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.MainOrder')),
            ],
        ),
        migrations.CreateModel(
            name='MainUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('email', models.CharField(max_length=25, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('pwd', models.CharField(max_length=200)),
                ('gender', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
                ('icon', models.ImageField(upload_to='icons')),
            ],
        ),
        migrations.AddField(
            model_name='mainorder',
            name='o_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.MainUser'),
        ),
        migrations.AddField(
            model_name='maincart',
            name='c_goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.MainGoods'),
        ),
        migrations.AddField(
            model_name='maincart',
            name='c_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.MainUser'),
        ),
    ]
