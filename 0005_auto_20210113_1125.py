# Generated by Django 2.1.7 on 2021-01-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_opday_optime'),
    ]

    operations = [
        migrations.AddField(
            model_name='dprofile',
            name='certificates',
            field=models.CharField(default=1234, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dprofile',
            name='f_url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
