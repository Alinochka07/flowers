# Generated by Django 3.2.6 on 2021-08-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowertypes', '0008_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='rosesbouquets',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='roses'),
        ),
    ]