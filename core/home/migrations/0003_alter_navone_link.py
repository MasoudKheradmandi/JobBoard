# Generated by Django 4.1.3 on 2023-03-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_navone_navtwo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navone',
            name='link',
            field=models.CharField(blank=True, max_length=100, verbose_name='لینک نوبار'),
        ),
    ]
