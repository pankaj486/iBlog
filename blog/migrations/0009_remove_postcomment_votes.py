# Generated by Django 3.2.8 on 2021-11-09 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_postcomment_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='votes',
        ),
    ]
