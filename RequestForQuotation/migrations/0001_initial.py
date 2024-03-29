# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-07 11:33
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        ('PurchaseRequisition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestForQuotation',
            fields=[
                ('request_for_quotation_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('time_created', models.DateTimeField()),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Person')),
                ('purchase_requisition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PurchaseRequisition.PurchaseRequisition')),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Vendor')),
            ],
        ),
        migrations.CreateModel(
            name='RequestForQuotationItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ref_id', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Item')),
                ('request_for_quotation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RequestForQuotation.RequestForQuotation')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='requestforquotationitem',
            unique_together=set([('request_for_quotation_id', 'item_id')]),
        ),
    ]
