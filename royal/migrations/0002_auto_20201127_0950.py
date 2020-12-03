# Generated by Django 3.1.3 on 2020-11-27 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='log_p',
            field=models.CharField(blank=True, max_length=20, verbose_name='login_password'),
        ),
        migrations.AddField(
            model_name='info',
            name='login_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(default='DEFAULT VALUE', max_length=50, verbose_name='username'),
        ),
    ]
