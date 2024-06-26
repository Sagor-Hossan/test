# Generated by Django 4.2.6 on 2024-06-23 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fit_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='foodmodel',
            name='date',
        ),
        migrations.AddField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ConsumedCalories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('calorie_consumed', models.FloatField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
