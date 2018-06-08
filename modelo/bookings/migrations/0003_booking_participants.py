# Generated by Django 2.0.4 on 2018-04-10 14:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0002_remove_booking_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='participants',
            field=models.ManyToManyField(related_name='item_participantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
