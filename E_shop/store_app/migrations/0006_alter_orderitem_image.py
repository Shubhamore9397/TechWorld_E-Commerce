# Generated by Django 5.0.7 on 2024-09-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
