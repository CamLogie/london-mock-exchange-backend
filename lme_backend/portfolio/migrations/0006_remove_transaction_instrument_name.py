# Generated by Django 3.1.4 on 2020-12-16 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='instrument_name',
        ),
    ]