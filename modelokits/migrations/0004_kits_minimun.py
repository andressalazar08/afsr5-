# Generated by Django 3.0.6 on 2020-08-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelokits', '0003_kits_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='kits',
            name='minimun',
            field=models.IntegerField(default=0),
        ),
    ]