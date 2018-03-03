# Generated by Django 2.0.2 on 2018-03-03 10:04

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='topicstatus',
            managers=[
                ('topic_statuses', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='meeting',
            unique_together={('topic', 'date')},
        ),
    ]
