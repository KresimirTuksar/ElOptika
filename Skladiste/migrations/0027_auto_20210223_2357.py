# Generated by Django 3.1.5 on 2021-02-23 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0026_auto_20210223_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='kabelutp',
            name='izdao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='kabelutphistory',
            name='izdao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
