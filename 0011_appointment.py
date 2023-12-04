# Generated by Django 2.1.7 on 2021-03-22 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0010_auto_20210321_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('Did', models.IntegerField()),
                ('Date', models.DateField()),
                ('token', models.IntegerField(default=0)),
                ('dis', models.CharField(default='not consulted', max_length=250)),
                ('med', models.CharField(default='not consulted', max_length=250)),
            ],
        ),
    ]
