# Generated by Django 5.1.6 on 2025-03-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('B_token', models.CharField(max_length=30)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='mpesa_transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MerchantRequestID', models.CharField(max_length=50, null=True)),
                ('CheckoutRequestID', models.CharField(max_length=50, null=True)),
                ('ResponseCode', models.CharField(max_length=30, null=True)),
                ('ResponseDescription', models.CharField(max_length=30, null=True)),
                ('CustomerMessage', models.CharField(max_length=30, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('amount', models.CharField(max_length=15, null=True)),
                ('paid_at', models.DateTimeField(auto_now_add=True)),
                ('account_reference', models.CharField(max_length=30)),
                ('transaction_desc', models.CharField(max_length=30)),
                ('occassion', models.CharField(max_length=30)),
                ('is_finished', models.BooleanField(default=False)),
                ('is_successful', models.BooleanField(default=False)),
                ('timestamp', models.IntegerField(null=True)),
                ('trans_id', models.CharField(max_length=30)),
            ],
            options={
                'get_latest_by': 'paid_at',
            },
        ),
    ]
