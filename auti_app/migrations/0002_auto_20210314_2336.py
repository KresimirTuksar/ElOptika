# Generated by Django 3.1.5 on 2021-03-14 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auti_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automobil',
            name='pocetna_kilometraza',
        ),
        migrations.RemoveField(
            model_name='automobil',
            name='registracija',
        ),
        migrations.RemoveField(
            model_name='automobil',
            name='zavrsna_kilometraza',
        ),
        migrations.RemoveField(
            model_name='kilometraza',
            name='automobil',
        ),
        migrations.AddField(
            model_name='automobil',
            name='datum',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='automobil',
            name='pocetna',
            field=models.IntegerField(blank=True, default=0, verbose_name='Kilometraža'),
        ),
        migrations.AddField(
            model_name='automobil',
            name='registracija_datum',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Tehnički'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='automobil',
            name='relacija',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='automobil',
            name='servis_datum',
            field=models.DateField(blank=True, null=True, verbose_name='Zadnji servis'),
        ),
        migrations.AddField(
            model_name='automobil',
            name='zavrsna',
            field=models.IntegerField(blank=True, default=0, verbose_name='Kilometraža'),
        ),
        migrations.AddField(
            model_name='kilometraza',
            name='ime',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='kilometraza',
            name='zaduzio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='automobil',
            name='servis_kilometri',
            field=models.IntegerField(blank=True, null=True, verbose_name='Servis na'),
        ),
        migrations.AlterField(
            model_name='automobil',
            name='tablica',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='kilometraza',
            name='datum',
            field=models.DateField(),
        ),
    ]
