# Generated by Django 4.1.5 on 2023-01-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapi', '0004_alter_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=220),
        ),
    ]
