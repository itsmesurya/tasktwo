# Generated by Django 2.1.5 on 2019-02-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_comment_parent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parenta_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]