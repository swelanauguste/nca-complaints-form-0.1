# Generated by Django 4.2.2 on 2023-06-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F'), ('RNS', 'RATHER NOT SAY')], default='RNS', max_length=3),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='goods_services',
            field=models.CharField(blank=True, max_length=255, verbose_name='Goods/Services'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='id_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='invoice_receipt_bill',
            field=models.CharField(blank=True, max_length=255, verbose_name='Invoice/Receipt/Bill'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='model_serial_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='Model/Serial number'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='phone1',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='redress',
            field=models.CharField(choices=[('R', 'REFUND'), ('X', 'EXCHANGE'), ('RR', 'REPAIR'), ('CN', 'CREDIT NOTE'), ('O', 'OTHER')], default='R', max_length=5),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='warranty_guaranty',
            field=models.CharField(blank=True, max_length=255, verbose_name='warranty/Guaranty'),
        ),
    ]
