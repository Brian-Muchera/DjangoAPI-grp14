# Generated by Django 3.1.3 on 2020-11-17 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group14', '0003_auto_20201116_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
    ]
