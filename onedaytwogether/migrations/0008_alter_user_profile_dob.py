# Generated by Django 4.2.2 on 2023-09-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onedaytwogether', '0007_shop_tour_purchase_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='dob',
            field=models.DateField(default='2023-09-03'),
        ),
    ]
