# Generated by Django 3.2.10 on 2022-02-17 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='media/profile/images/default.jpg', null=True, upload_to='media/profile/images'),
        ),
    ]