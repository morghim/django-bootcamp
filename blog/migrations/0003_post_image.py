# Generated by Django 4.0.1 on 2022-02-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_pub_date_post_slug_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]