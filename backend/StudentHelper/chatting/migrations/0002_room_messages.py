# Generated by Django 5.0.4 on 2024-05-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='messages',
            field=models.TextField(blank=True, null=True),
        ),
    ]
