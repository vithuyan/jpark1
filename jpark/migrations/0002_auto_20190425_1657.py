# Generated by Django 2.1.5 on 2019-04-25 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jpark', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='ending_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='starting_date',
        ),
    ]
