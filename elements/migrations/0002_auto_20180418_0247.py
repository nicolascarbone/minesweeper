# Generated by Django 2.0.4 on 2018-04-18 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='cell',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='element',
            name='row',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
