# Generated by Django 2.2.1 on 2019-06-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Download_file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_resize',
            name='oldSize',
            field=models.CharField(max_length=12, null=0),
        ),
    ]
