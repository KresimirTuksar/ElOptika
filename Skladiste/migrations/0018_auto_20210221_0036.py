# Generated by Django 3.1.5 on 2021-02-20 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0017_auto_20210221_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kabeloptika',
            name='zadnje_osvjezeno',
            field=models.DateTimeField(auto_now=True, verbose_name='Posljednje ažuriranje'),
        ),
        migrations.AlterField(
            model_name='kabeloptikahistory',
            name='zadnje_osvjezeno',
            field=models.DateTimeField(null=True, verbose_name='Posljednje ažuriranje'),
        ),
    ]