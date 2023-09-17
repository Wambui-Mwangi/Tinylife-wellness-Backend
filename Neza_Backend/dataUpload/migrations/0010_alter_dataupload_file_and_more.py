# Generated by Django 4.2.5 on 2023-09-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataUpload', '0009_alter_extracteddata_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupload',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='extracteddata',
            name='past_cases_of_lead_poisoning',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='extracteddata',
            name='proximity_to_dumpsite',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='extracteddata',
            name='proximity_to_industries',
            field=models.CharField(max_length=255),
        ),
    ]
