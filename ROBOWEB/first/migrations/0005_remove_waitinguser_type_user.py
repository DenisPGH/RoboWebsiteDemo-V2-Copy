# Generated by Django 4.0.3 on 2022-04-11 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_alter_waitinguser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waitinguser',
            name='type_user',
        ),
    ]
