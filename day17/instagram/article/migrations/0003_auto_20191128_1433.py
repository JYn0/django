# Generated by Django 2.2.7 on 2019-11-28 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_article_titles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_titles',
            new_name='user_likes',
        ),
    ]
