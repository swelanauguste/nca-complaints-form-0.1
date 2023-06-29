# Generated by Django 4.2.2 on 2023-06-28 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('summary', models.CharField(max_length=50)),
                ('id_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=11)),
                ('phone1', models.CharField(max_length=11)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('RNS', 'RATHER_NOT_SAY')], default='RNS', max_length=3)),
                ('age_group', models.CharField(choices=[('13 - 17', '13 - 17'), ('18 - 25', '18 - 25'), ('26 - 35', '26 - 35'), ('36 - 50', '36 - 50'), ('OVER 50', 'over 50')], default='OVER 50', max_length=7)),
                ('business_name', models.CharField(max_length=255)),
                ('business_address', models.CharField(blank=True, max_length=255)),
                ('business_sector', models.CharField(blank=True, max_length=255)),
                ('contact_person', models.CharField(blank=True, max_length=255)),
                ('business_phone', models.CharField(blank=True, max_length=11)),
                ('business_email', models.EmailField(blank=True, max_length=254)),
                ('goods_services', models.CharField(blank=True, max_length=255)),
                ('model_serial_number', models.CharField(blank=True, max_length=255)),
                ('category', models.CharField(blank=True, max_length=255)),
                ('date_purchased', models.DateField(blank=True)),
                ('warranty_guaranty', models.CharField(blank=True, max_length=255)),
                ('brand', models.CharField(blank=True, max_length=255)),
                ('brand_code', models.CharField(blank=True, max_length=255)),
                ('invoice_receipt_bill', models.CharField(blank=True, max_length=255)),
                ('manufactured_date', models.DateField(blank=True)),
                ('standard', models.CharField(blank=True, max_length=255)),
                ('electrical_frequency_rating', models.CharField(blank=True, max_length=255)),
                ('voltage_required', models.CharField(blank=True, max_length=255)),
                ('complaint', models.TextField()),
                ('redress', models.CharField(choices=[('R', 'REFUND'), ('X', 'EXCHANGE'), ('RR', 'REPAIR'), ('CN', 'CREDIT_NOTE'), ('O', 'OTHER')], default='R', max_length=5)),
                ('other_redress', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintHandling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officer', models.CharField(blank=True, max_length=255)),
                ('investigating_officer', models.CharField(blank=True, max_length=255)),
                ('ministry_liaison', models.CharField(blank=True, max_length=255)),
                ('date', models.DateField()),
                ('exhibits', models.TextField()),
                ('results', models.TextField()),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='handling', to='core.complaint')),
            ],
        ),
    ]
