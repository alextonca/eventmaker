# Generated by Django 2.2.17 on 2021-04-05 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventmakerapp', '0002_event_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='amount_likes',
        ),
    ]
