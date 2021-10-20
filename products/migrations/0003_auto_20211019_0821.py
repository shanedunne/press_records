# Generated by Django 3.2.8 on 2021-10-19 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='album_name',
        ),
        migrations.AddField(
            model_name='product',
            name='artist_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]