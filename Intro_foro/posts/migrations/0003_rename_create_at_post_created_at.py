# Generated by Django 4.2.4 on 2023-10-26 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_post_comment_user_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_at',
            new_name='created_at',
        ),
    ]