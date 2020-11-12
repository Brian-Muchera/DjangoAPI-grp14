# Generated by Django 3.1.3 on 2020-11-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_id', models.CharField(max_length=50)),
                ('patient_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1)),
                ('age', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Patient',
                'ordering': ['-pt_id'],
            },
        ),
    ]
