# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_subscription_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.CharField(max_length=100),
        ),
    ]
