# Generated by Django 5.1.6 on 2025-03-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0001_initial'),

    ]

    operations = [
        migrations.AddField(
            model_name='investimento',
            name='nivel',
            field=models.IntegerField(default=1),
        ),
    ]
