# Generated by Django 3.2.9 on 2021-11-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_remove_product_bg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('company_size', models.CharField(choices=[('1', '1-10'), ('2', '11-50'), ('3', '51-200'), ('4', '201-500')], max_length=255)),
                ('industry', models.CharField(choices=[('1', 'Agriculture'), ('2', 'Banking & Finance'), ('3', 'Business Services & Softwares')], max_length=255)),
                ('job_role', models.CharField(choices=[('1', 'C-Suite'), ('2', 'VIP')], max_length=255)),
                ('country', models.CharField(choices=[('us', 'United States'), ('al', 'Albania')], max_length=255)),
                ('user_agreement', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'web_contact',
                'ordering': ['-id'],
            },
        ),
    ]
