# Generated by Django 5.0.4 on 2024-04-26 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='dataId',
        ),
    ]