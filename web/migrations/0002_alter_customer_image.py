# Generated by Django 3.2.9 on 2021-11-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.FileField(upload_to='Customer/'),
        ),
    ]