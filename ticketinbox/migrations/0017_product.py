# Generated by Django 2.2.12 on 2021-04-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketinbox', '0016_auto_20210410_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('product_catogary', models.CharField(choices=[('clothing', 'clothing'), ('accessories', 'accessories'), ('footwear', 'footwear')], max_length=200)),
            ],
        ),
    ]
