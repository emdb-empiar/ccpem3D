# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=100)),
                ('vtp_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/', location=b'/Users/pkorir/Documents/workspace/ccpem3D/view3D/files'), upload_to=b'')),
            ],
        ),
    ]
