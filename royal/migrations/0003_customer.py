# Generated by Django 3.1.3 on 2020-11-27 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('royal', '0002_auto_20201127_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=50, verbose_name='customer name')),
                ('phone', models.BigIntegerField()),
                ('address', models.CharField(max_length=100, verbose_name='customer address')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='royal.info')),
            ],
        ),
    ]
