# Generated by Django 4.0.4 on 2022-04-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_auto_20220416_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='source',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]