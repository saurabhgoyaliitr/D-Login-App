# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.CharField(max_length=200, choices=[(b'CSE', b'CSE'), (b'ECE', b'ECE'), (b'EE', b'EE'), (b'ME', b'ME')])),
                ('enrollment', models.IntegerField()),
                ('gender', models.CharField(default=b'Male', max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('dob', models.DateField()),
                ('contact', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=300)),
                ('profile', models.ImageField(default=b'/profile/default.jpg', upload_to=b'./profile/')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
