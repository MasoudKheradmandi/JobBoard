# Generated by Django 4.1.7 on 2023-04-08 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_user_token'),
        ('job', '0006_jobcategory_class_icon'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0003_sendresume_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendresume',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.job'),
        ),
        migrations.AlterField(
            model_name='sendresume',
            name='reciver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company'),
        ),
        migrations.AlterField(
            model_name='sendresume',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
