# Generated by Django 5.1 on 2024-08-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='raiting',
            new_name='rating',
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]