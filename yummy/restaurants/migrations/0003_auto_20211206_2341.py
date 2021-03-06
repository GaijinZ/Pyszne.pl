# Generated by Django 3.2.8 on 2021-12-06 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20211027_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='price_to_deliver',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='delivery',
            name='time_to_deliver',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='delivery',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='restaurants.delivery'),
            preserve_default=False,
        ),
    ]
