# Generated by Django 5.0.4 on 2024-04-26 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
