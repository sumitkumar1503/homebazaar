# Generated by Django 3.0.5 on 2021-11-28 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoryname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]