# Generated by Django 4.2.6 on 2023-10-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tech', '0002_post_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
