# Generated by Django 3.0.3 on 2021-02-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='post/content_pictures'),
        ),
    ]