# Generated by Django 2.0.3 on 2020-04-26 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipmentitem',
            old_name='shipment_id',
            new_name='shipment',
        ),
    ]
