# Generated by Django 3.0.8 on 2020-11-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.CharField(default='', max_length=65),
        ),
    ]