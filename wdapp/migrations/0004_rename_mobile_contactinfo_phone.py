# Generated by Django 3.2.4 on 2021-08-26 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wdapp', '0003_rename_contact_contactinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='mobile',
            new_name='phone',
        ),
    ]