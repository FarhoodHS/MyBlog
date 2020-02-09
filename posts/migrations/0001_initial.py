# Generated by Django 2.2.7 on 2020-02-04 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location)),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_updated', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]