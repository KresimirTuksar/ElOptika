# Generated by Django 3.1.5 on 2021-02-14 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0008_auto_20210214_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skladiste',
            name='zaduzio',
        ),
        migrations.RemoveField(
            model_name='skladistehistory',
            name='zaduzio',
        ),
    ]