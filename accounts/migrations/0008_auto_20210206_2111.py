# Generated by Django 2.2.3 on 2021-02-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210206_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='pruduct',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]