# Generated by Django 3.2.9 on 2021-11-17 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_feature'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelTable(
            name='feature',
            table='web_feature',
        ),
    ]
