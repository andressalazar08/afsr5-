# Generated by Django 3.0.6 on 2020-08-26 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelokits', '0009_auto_20200821_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='kit_beneciciary',
            name='date_asignacion',
            field=models.DateTimeField(null=True),
        ),
    ]
