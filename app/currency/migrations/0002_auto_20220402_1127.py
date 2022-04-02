# Generated by Django 2.2.12 on 2022-04-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=40)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]