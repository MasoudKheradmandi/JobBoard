# Generated by Django 4.1.3 on 2023-03-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_ostan_delete_ostan'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
