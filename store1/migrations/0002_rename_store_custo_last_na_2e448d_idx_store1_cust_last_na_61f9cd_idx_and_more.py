# Generated by Django 4.2 on 2023-05-02 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store1', '0001_initial'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='customer',
            new_name='store1_cust_last_na_61f9cd_idx',
            old_name='store_custo_last_na_2e448d_idx',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store1_customer',
        ),
    ]
