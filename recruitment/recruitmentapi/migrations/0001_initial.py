# Generated by Django 4.2.7 on 2023-11-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('personal_email', models.CharField(max_length=100)),
                ('kiet_email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('mode_of_payment', models.CharField(max_length=100)),
                ('library_id', models.CharField(max_length=100)),
                ('desk', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
    ]
