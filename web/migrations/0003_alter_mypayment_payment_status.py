# Generated by Django 3.2.25 on 2024-12-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20241118_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypayment',
            name='Payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('expired', 'expired')], default='pending', max_length=10),
        ),
    ]
