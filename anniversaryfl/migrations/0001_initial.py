# Generated by Django 3.2.6 on 2021-08-27 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WeddingBouquetFlowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='wedding')),
                ('sale', models.IntegerField(blank=True, default=0, null=True, verbose_name='Discount percentage')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Свадебный букет',
                'verbose_name_plural': 'Свадебные букеты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HundredRoseFlowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hundredroses')),
                ('sale', models.IntegerField(blank=True, default=0, null=True, verbose_name='Discount percentage')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '101 роза',
                'verbose_name_plural': 'Букеты из 101 роз',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BasketBouquetFlowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='basketflower')),
                ('sale', models.IntegerField(blank=True, default=0, null=True, verbose_name='Discount percentage')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Букет в корзинке',
                'verbose_name_plural': 'Букеты в корзинках',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AnniversaryFlowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='anniversary')),
                ('sale', models.IntegerField(blank=True, default=0, null=True, verbose_name='Discount percentage')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Букет на торжество',
                'verbose_name_plural': 'Букеты на торжество',
                'ordering': ['name'],
            },
        ),
    ]
