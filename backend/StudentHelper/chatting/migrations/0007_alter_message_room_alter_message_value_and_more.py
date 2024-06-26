# Generated by Django 5.0.4 on 2024-05-05 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0006_alter_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_messages', to='chatting.room'),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='room',
            name='messages',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
