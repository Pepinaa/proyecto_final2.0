# Generated by Django 4.2.4 on 2023-10-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_post_options_rename_publised_post_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/media/images/default.png', upload_to='images/'),
        ),
    ]
