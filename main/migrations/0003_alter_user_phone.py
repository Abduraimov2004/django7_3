# Generated by Django 5.1 on 2024-08-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_tag_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, db_index=True, max_length=13, null=True, unique=True),
        ),
    ]
