# Generated by Django 2.1 on 2018-10-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20181009_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo_file',
            field=models.ImageField(default='{{ STATIC_URL }}img/banff_mountain.jpg', upload_to='{{ STATIC_URL }}img/photos'),
        ),
    ]
