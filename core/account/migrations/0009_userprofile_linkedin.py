# Generated by Django 4.1.3 on 2023-02-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_userprofile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
    ]