# Generated by Django 3.1.5 on 2021-02-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0006_auto_20210214_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skladistehistory',
            name='zadnje_osvjezeno',
            field=models.DateField(null=True),
        ),
    ]