# Generated by Django 4.2.4 on 2023-10-26 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('publised', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
