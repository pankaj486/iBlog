# Generated by Django 3.2.8 on 2021-11-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='My_blog.jpg', null=True, upload_to='images/'),
        ),
    ]