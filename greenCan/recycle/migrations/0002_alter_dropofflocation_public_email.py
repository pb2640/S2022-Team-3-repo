# Generated by Django 4.0.1 on 2022-03-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropofflocation',
            name='public_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]