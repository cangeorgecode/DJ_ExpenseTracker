# Generated by Django 5.0.4 on 2024-05-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
