# Generated by Django 2.1.7 on 2021-02-07 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_auto_20210113_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dprofile',
            old_name='f_url',
            new_name='furl',
        ),
    ]
