# Generated by Django 3.1.5 on 2021-02-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0002_auto_20210228_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alat',
            name='inv_broj',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Inventurni broj'),
        ),
    ]