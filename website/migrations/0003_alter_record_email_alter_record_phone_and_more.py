# Generated by Django 4.2.6 on 2023-10-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_alter_record_phone_alter_record_zipcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="email",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="record",
            name="phone",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="record",
            name="zipcode",
            field=models.CharField(max_length=50),
        ),
    ]
