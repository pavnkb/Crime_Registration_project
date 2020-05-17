# Generated by Django 3.0.2 on 2020-01-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_auto_20200127_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbtable',
            name='name_repoter',
        ),
        migrations.AddField(
            model_name='dbtable',
            name='name_reporter',
            field=models.CharField(default='user', max_length=100),
        ),
        migrations.AlterField(
            model_name='dbtable',
            name='Time_reported',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='dbtable',
            name='crime_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dbtable',
            name='date_crime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dbtable',
            name='date_reported',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dbtable',
            name='email_reporter',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dbtable',
            name='phone_reporter',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='dbtable',
            name='time_crime',
            field=models.TimeField(),
        ),
    ]