# Generated by Django 5.0.3 on 2024-03-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0010_vendor_book_desc_vendor_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
