# Generated by Django 4.2.6 on 2023-10-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tech', '0006_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=1000),
        ),
    ]
