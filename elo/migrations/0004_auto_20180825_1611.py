# Generated by Django 2.0.8 on 2018-08-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elo', '0003_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
