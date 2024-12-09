# Generated by Django 4.2.17 on 2024-12-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='available',
        ),
        migrations.RemoveField(
            model_name='car',
            name='model',
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
    ]
