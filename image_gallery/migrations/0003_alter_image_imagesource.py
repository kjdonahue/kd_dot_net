# Generated by Django 4.0.1 on 2022-01-20 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_gallery', '0002_rename_isfrontpage_image_showonfrontpage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageSource',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
