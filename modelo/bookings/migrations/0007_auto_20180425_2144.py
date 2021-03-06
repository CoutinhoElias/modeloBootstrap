# Generated by Django 2.0.4 on 2018-04-25 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0006_auto_20180424_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='participants',
        ),
        migrations.AddField(
            model_name='booking',
            name='participants',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
