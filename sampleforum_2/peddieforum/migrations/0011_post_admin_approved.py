# Generated by Django 3.1.7 on 2021-04-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peddieforum', '0010_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]