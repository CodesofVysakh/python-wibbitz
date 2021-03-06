# Generated by Django 3.2.9 on 2021-11-18 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_product_bg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='company_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='designation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='is_featured',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='logo',
            field=models.FileField(null=True, upload_to='Testimonial/logos'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
