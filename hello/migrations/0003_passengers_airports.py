# Generated by Django 4.0.4 on 2023-01-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_airport_flight_passengers'),
    ]

    operations = [
        migrations.AddField(
            model_name='passengers',
            name='airports',
            field=models.ManyToManyField(related_name='airports', to='hello.airport'),
        ),
    ]
