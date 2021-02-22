# Generated by Django 3.1.5 on 2021-02-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0020_auto_20210221_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kabeloptika',
            name='broj_niti',
            field=models.IntegerField(blank=True, null=True, verbose_name='Broj niti'),
        ),
        migrations.AlterField(
            model_name='kabeloptika',
            name='inv_broj',
            field=models.IntegerField(blank=True, null=True, verbose_name='Inventurni broj'),
        ),
        migrations.AlterField(
            model_name='kabeloptika',
            name='izdana_metraza',
            field=models.IntegerField(blank=True, null=True, verbose_name='Izdano metara'),
        ),
        migrations.AlterField(
            model_name='kabeloptikahistory',
            name='broj_niti',
            field=models.IntegerField(default=1, verbose_name='Broj niti'),
        ),
        migrations.AlterField(
            model_name='kabeloptikahistory',
            name='inv_broj',
            field=models.IntegerField(blank=True, null=True, verbose_name='Inventurni broj'),
        ),
        migrations.AlterField(
            model_name='kabeloptikahistory',
            name='izdana_metraza',
            field=models.IntegerField(blank=True, null=True, verbose_name='Izdano metara'),
        ),
        migrations.AlterField(
            model_name='kabeloptikahistory',
            name='metraza',
            field=models.IntegerField(default=0, verbose_name='Ukupna metraža'),
        ),
    ]
