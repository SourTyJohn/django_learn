# Generated by Django 5.0.3 on 2024-04-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_blogmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmessage',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]