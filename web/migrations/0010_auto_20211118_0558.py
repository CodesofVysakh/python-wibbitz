# Generated by Django 3.2.9 on 2021-11-18 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20211118_0546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelTable(
            name='testimonial',
            table='web_testimonial',
        ),
    ]
