# Generated by Django 4.1.7 on 2023-04-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_key'),
        ('account', '0016_userprofile_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key',
            field=models.ManyToManyField(blank=True, to='job.key'),
        ),
    ]
