# Generated by Django 3.1.5 on 2021-02-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0022_auto_20210223_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kabelbakar',
            name='inv_broj',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Inventurni broj'),
        ),
    ]
