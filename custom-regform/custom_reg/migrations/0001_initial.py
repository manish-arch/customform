# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TMC_NO', models.IntegerField(verbose_name=b'TMC NO', error_messages={b'required': 'Pleae Enter Your TMC NO'})),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
