# Generated by Django 4.2.6 on 2024-06-26 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fit_app', '0006_consumedcalories_total_calorie_consumed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumedcalories',
            name='total_calorie_consumed',
        ),
    ]
