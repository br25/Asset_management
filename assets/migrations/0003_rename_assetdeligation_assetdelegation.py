# Generated by Django 4.1.3 on 2022-12-02 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('assets', '0002_remove_assetdeligation_handover_at_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssetDeligation',
            new_name='AssetDelegation',
        ),
    ]