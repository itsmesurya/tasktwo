# Generated by Django 2.1.5 on 2019-02-13 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0016_auto_20190213_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('key', models.CharField(max_length=32)),
                ('score', models.SmallIntegerField(choices=[(-1, 'DISLIKE'), (1, 'LIKE')])),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_changed', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updown_votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('object_id', 'key', 'user')},
        ),
    ]
