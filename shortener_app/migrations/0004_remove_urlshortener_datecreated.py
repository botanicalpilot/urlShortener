# Generated by Django 3.0.1 on 2020-01-02 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0003_auto_20191231_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlshortener',
            name='dateCreated',
        ),
    ]
