# Generated by Django 2.2.7 on 2019-12-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
