# Generated by Django 2.2 on 2019-04-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20190408_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image_url',
            field=models.TextField(blank=True),
        ),
    ]