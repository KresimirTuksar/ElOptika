# Generated by Django 3.1.5 on 2021-02-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0019_auto_20210221_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kabeloptika',
            name='broj_niti',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Broj niti'),
        ),
        migrations.AlterField(
            model_name='kabeloptika',
            name='metraza',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Ukupna metraža'),
        ),
    ]
