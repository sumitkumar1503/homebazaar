# Generated by Django 3.0.5 on 2021-11-28 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0006_auto_20211128_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='categoryname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
