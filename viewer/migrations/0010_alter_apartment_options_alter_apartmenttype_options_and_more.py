# Generated by Django 4.2.16 on 2024-09-23 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0009_rename_property_property_property_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='apartmenttype',
            options={'ordering': ['property_type']},
        ),
        migrations.AlterModelOptions(
            name='cities',
            options={'ordering': ['name'], 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='ground',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='groundtype',
            options={'ordering': ['property_type']},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='housetype',
            options={'ordering': ['property_type']},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.RemoveField(
            model_name='property',
            name='bit',
        ),
        migrations.AlterField(
            model_name='house',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='garden_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='plot_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='property_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houses', to='viewer.housetype'),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='property_type',
            field=models.CharField(max_length=15),
        ),
    ]
