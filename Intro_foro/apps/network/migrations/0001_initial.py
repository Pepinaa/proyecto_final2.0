# Generated by Django 4.2.4 on 2023-11-26 02:13

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('identifier', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.IntegerField()),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
