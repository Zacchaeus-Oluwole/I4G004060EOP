# Generated by Django 4.0 on 2022-07-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Published_date',
            field=models.DateTimeField(),
        ),
    ]
