# Generated by Django 3.1 on 2021-10-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='product',
            name='descrtiption',
            field=models.TextField(blank=True, max_length=800),
        ),
    ]
