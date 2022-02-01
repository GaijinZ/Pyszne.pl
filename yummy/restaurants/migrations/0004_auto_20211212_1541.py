# Generated by Django 3.2.8 on 2021-12-12 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20211206_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=250)),
                ('post_code', models.IntegerField()),
                ('street_name', models.CharField(max_length=250)),
                ('building_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.address'),
            preserve_default=False,
        ),
    ]
