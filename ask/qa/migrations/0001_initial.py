# Generated by Django 3.2.7 on 2021-09-17 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(default=0)),
                ('likes', models.ManyToManyField(related_name='likes_question', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects_new', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question')),
            ],
        ),
    ]
