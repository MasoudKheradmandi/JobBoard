# Generated by Django 4.1.3 on 2023-03-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_telecommuting'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcategory',
            name='class_icon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]