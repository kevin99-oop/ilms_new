# Generated by Django 4.0.2 on 2022-04-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20220406_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='credit_score',
            field=models.CharField(default='300', max_length=3),
            preserve_default=False,
        ),
    ]
