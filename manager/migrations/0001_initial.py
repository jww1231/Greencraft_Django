# Generated by Django 5.0.1 on 2024-02-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('managercode', models.CharField(max_length=20, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('gasoline_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('phone_number', models.CharField(max_length=15)),
                ('pump_number', models.IntegerField()),
            ],
        ),
    ]