# Generated by Django 3.0.6 on 2020-06-10 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predatoryjournals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='added_date',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='text',
        ),
    ]