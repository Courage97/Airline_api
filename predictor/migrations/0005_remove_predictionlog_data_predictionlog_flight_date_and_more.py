# Generated by Django 5.2.1 on 2025-05-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0004_predictionlog_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictionlog',
            name='data',
        ),
        migrations.AddField(
            model_name='predictionlog',
            name='flight_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictionlog',
            name='flight_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='predictionlog',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='predictionlog',
            name='note_to_attendant',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictionlog',
            name='seat_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
