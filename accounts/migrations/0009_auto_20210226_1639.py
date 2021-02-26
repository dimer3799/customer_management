# Generated by Django 2.2.3 on 2021-02-26 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210206_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег товара', 'verbose_name_plural': 'Теги товара'},
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Pruduct', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='pruduct',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание'),
        ),
    ]
