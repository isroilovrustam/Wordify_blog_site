# Generated by Django 4.1.5 on 2023-01-31 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalpicture',
            name='is_vite',
            field=models.BooleanField(default=True),
        ),
    ]
