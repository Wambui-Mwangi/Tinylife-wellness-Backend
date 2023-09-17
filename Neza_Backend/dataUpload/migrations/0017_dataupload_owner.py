# Generated by Django 4.2.5 on 2023-09-15 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataUpload', '0016_alter_extracteddata_file_hash_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataupload',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
