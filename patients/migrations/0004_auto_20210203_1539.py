# Generated by Django 3.1.5 on 2021-02-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_patient_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='test_result',
            field=models.CharField(choices=[('Negative', 'Negative'), ('Positive', 'Positive'), ('Awaiting', 'Awaiting')], default='Awaiting', max_length=100),
        ),
    ]
