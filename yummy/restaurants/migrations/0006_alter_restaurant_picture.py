# Generated by Django 3.2.8 on 2022-01-10 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_alter_address_post_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='picture',
            field=models.ImageField(blank=True, upload_to='restaurant_picture'),
        ),
    ]
