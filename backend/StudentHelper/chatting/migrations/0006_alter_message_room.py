# Generated by Django 5.0.4 on 2024-05-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0005_alter_message_room_alter_message_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.BigIntegerField(),
        ),
    ]