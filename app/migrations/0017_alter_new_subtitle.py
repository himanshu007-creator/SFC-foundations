# Generated by Django 3.2 on 2021-05-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_news_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='subtitle',
            field=models.URLField(),
        ),
    ]