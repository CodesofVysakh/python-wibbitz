# Generated by Django 3.2.9 on 2021-11-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_blog_title_redirection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingfeature',
            name='image',
            field=models.FileField(upload_to='MarketingFeature/images'),
        ),
    ]
