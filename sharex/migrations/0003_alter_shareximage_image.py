# Generated by Django 4.0.5 on 2022-06-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharex', '0002_remove_shareximage_uploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareximage',
            name='image',
            field=models.ImageField(upload_to='static/sharex/images/'),
        ),
    ]
