# Generated by Django 2.2.3 on 2021-02-01 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_pruduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruduct',
            name='category',
            field=models.CharField(choices=[('Для дома', 'Для дома'), ('Для улицы', 'Для улицы')], max_length=200, null=True),
        ),
    ]
