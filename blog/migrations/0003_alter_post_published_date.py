# Generated by Django 4.0 on 2022-07-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
