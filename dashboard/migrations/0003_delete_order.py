# Generated by Django 4.0.1 on 2022-01-15 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]