# Generated by Django 3.1.7 on 2021-03-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210306_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='name',
            field=models.CharField(default='Wallet', max_length=20),
            preserve_default=False,
        ),
    ]