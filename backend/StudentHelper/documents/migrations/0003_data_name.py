# Generated by Django 5.0.4 on 2024-04-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_remove_data_dataid'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='name',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
