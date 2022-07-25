# Generated by Django 4.0.4 on 2022-06-07 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_otpmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="otpmodel",
            name="otp_qr",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="otpmodel",
            name="key",
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
