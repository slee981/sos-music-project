# Generated by Django 2.2.6 on 2019-12-08 01:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0008_auto_20191207_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='songcomment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='songcomment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
