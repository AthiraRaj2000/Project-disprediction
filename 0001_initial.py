# Generated by Django 2.1.7 on 2021-01-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dprofile',
            fields=[
                ('Did', models.AutoField(primary_key=True, serialize=False)),
                ('Lno', models.CharField(max_length=100)),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('qualification', models.CharField(max_length=100)),
                ('spc', models.CharField(max_length=100)),
                ('exp', models.DateField()),
                ('hname', models.CharField(max_length=100)),
                ('cname', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
            ],
        ),
    ]
