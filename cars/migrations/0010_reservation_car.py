# Generated by Django 4.2 on 2024-12-10 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='car',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, related_name='car_reservations', to='cars.car'),
        ),
    ]
