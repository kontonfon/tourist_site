# Generated by Django 3.1.6 on 2021-02-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_payment_intent'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='used_coupon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
