# Generated by Django 2.1.7 on 2019-04-25 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jpark', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parking',
            options={'permissions': (('can_edit_parking', 'User Can edit Parking'),)},
        ),
        migrations.RemoveField(
            model_name='parking',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='parking',
            name='lng',
        ),
    ]
