# Generated by Django 4.1.7 on 2023-03-20 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_rename_vendor_nmae_vendor_vendor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
