# Generated by Django 4.1.4 on 2023-01-26 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_rename_admin_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('query', models.CharField(max_length=255)),
            ],
        ),
    ]
