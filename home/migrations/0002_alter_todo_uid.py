# Generated by Django 5.1.1 on 2024-10-11 08:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a7b08778-99c1-408f-a7dd-9217e627bb11'), editable=False, primary_key=True, serialize=False),
        ),
    ]
