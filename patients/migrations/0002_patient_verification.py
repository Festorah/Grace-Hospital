# Generated by Django 3.1.5 on 2021-02-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='verification',
            field=models.CharField(default='osun', max_length=200),
        ),
    ]
