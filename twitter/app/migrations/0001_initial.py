# Generated by Django 4.1.7 on 2024-01-09 16:49

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(default=app.models.generate_random_number, max_length=20, unique=True)),
            ],
        ),
    ]
