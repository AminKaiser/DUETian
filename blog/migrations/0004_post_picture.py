# Generated by Django 3.0.3 on 2021-02-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210211_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to='post/content_pictures'),
        ),
    ]