# Generated by Django 3.2.7 on 2021-09-25 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20210925_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
