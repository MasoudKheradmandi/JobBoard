# Generated by Django 4.1.7 on 2023-04-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_sendresume_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendresume',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]