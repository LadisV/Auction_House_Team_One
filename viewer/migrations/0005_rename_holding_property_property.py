# Generated by Django 4.2.16 on 2024-09-20 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_rename_property_property_holding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='holding',
            new_name='property',
        ),
    ]
