# Generated by Django 4.1.3 on 2023-03-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_telecommuting'),
        ('account', '0011_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wish_list',
            field=models.ManyToManyField(to='job.job'),
        ),
    ]
