# Generated by Django 4.2.6 on 2023-10-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
    ]
