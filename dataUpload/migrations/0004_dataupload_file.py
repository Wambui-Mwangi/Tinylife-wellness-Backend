# Generated by Django 4.2.5 on 2023-09-08 04:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dataUpload', '0003_alter_dataupload_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataupload',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]