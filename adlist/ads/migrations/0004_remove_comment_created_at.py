# Generated by Django 2.1.7 on 2019-04-08 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20190407_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]
