# Generated by Django 3.0.6 on 2020-09-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelokits', '0012_kitsprincipal'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitsproducts',
            name='quantity_substitute',
            field=models.IntegerField(default=0),
        ),
    ]
