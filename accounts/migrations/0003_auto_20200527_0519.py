# Generated by Django 3.0.5 on 2020-05-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200513_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
