# Generated by Django 3.1.5 on 2021-02-20 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0015_auto_20210220_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kabelbakar',
            old_name='ukupna_metraza',
            new_name='metraza',
        ),
        migrations.RenameField(
            model_name='kabeloptika',
            old_name='ukupna_metraza',
            new_name='metraza',
        ),
        migrations.RenameField(
            model_name='kabelutp',
            old_name='ukupna_metraza',
            new_name='metraza',
        ),
        migrations.RemoveField(
            model_name='kabelbakar',
            name='preostala_metraza',
        ),
        migrations.RemoveField(
            model_name='kabeloptika',
            name='preostala_metraza',
        ),
        migrations.RemoveField(
            model_name='kabelutp',
            name='preostala_metraza',
        ),
    ]
