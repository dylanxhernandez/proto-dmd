# Generated by Django 5.0.2 on 2024-05-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto_dmd_app', '0002_markdowncontent_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markdowncontent',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
