# Generated by Django 4.0.5 on 2022-06-10 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharex', '0004_alter_shareximage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharexToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sharex_tokens', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
