# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 00:18
from __future__ import unicode_literals

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
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_assigned', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('listing_dscr', models.TextField(max_length=500)),
                ('amount_listed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('assigned_date', models.DateTimeField(blank=True, null=True)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('listee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_offered', models.DecimalField(decimal_places=2, max_digits=6)),
                ('amount_accepted', models.DecimalField(decimal_places=2, max_digits=6)),
                ('trade_choices', models.CharField(choices=[(b'AC', b'Accept'), (b'WT', b'Wait'), (b'DC', b'Decline'), (b'WD', b'Withdraw')], default=b'AC', max_length=2)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.Listing')),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
