# Generated by Django 5.2 on 2025-04-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pierre_CMS_App', '0015_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsettings',
            name='contact_email',
            field=models.EmailField(default='contact@pierrecustomer.com', max_length=200, null=True),
        ),
    ]
