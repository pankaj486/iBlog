# Generated by Django 3.2.8 on 2021-11-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='My_blog.jpg', null=True, upload_to='images/'),
        ),
    ]
