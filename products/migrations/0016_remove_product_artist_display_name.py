# Generated by Django 3.2.8 on 2021-11-20 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_artist_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='artist_display_name',
        ),
    ]
