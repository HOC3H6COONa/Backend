# Generated by Django 4.1.1 on 2024-02-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_user_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.DecimalField(decimal_places=12, default=None, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.DecimalField(decimal_places=12, default=None, max_digits=15, null=True),
        ),
    ]