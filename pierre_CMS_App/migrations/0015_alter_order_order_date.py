# Generated by Django 5.2 on 2025-04-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pierre_CMS_App', '0014_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
