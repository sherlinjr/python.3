# Generated by Django 4.1.5 on 2023-01-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-10-16'),
            preserve_default=False,
        ),
    ]