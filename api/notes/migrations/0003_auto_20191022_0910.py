# Generated by Django 2.2.6 on 2019-10-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20191022_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(blank=True, default=''),
        ),
    ]
