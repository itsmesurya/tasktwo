# Generated by Django 2.1.5 on 2019-02-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_post_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_time']},
        ),
        migrations.AddField(
            model_name='comment',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]