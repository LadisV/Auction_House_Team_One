# Generated by Django 5.1.1 on 2024-09-24 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_remove_bid_property_auction_bid_auction_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={},
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='viewer.apartment')),
                ('auctions', models.ManyToManyField(blank=True, related_name='images', to='viewer.auction')),
                ('ground', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='viewer.ground')),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='viewer.house')),
            ],
        ),
    ]
