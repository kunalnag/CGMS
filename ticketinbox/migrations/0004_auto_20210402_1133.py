# Generated by Django 3.1.5 on 2021-04-02 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketinbox', '0003_auto_20210401_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='due',
            new_name='due_date',
        ),
    ]
