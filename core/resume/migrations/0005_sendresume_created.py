# Generated by Django 4.1.7 on 2023-04-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_alter_sendresume_post_alter_sendresume_reciver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendresume',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
