# Generated by Django 3.2.5 on 2021-09-21 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='notes.tag'),
            preserve_default=False,
        ),
    ]
