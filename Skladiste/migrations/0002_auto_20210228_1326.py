# Generated by Django 3.1.5 on 2021-02-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skladiste', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alat',
            name='izdao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='zaduzenja',
            name='datum_zaduzivanja',
            field=models.DateField(verbose_name='Zaduženo dana'),
        ),
        migrations.AlterField(
            model_name='zaduzenja',
            name='kreirano',
            field=models.DateTimeField(),
        ),
    ]