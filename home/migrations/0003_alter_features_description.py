# Generated by Django 4.0.1 on 2022-01-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='description',
            field=models.CharField(max_length=60),
        ),
    ]
