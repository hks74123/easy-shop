# Generated by Django 4.0.3 on 2022-11-19 20:47

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
            name='Dukaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField()),
                ('intro', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='imgs')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=60)),
                ('seller_address', models.TextField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('dukaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.dukaan')),
                ('images', models.ManyToManyField(to='mainApp.image')),
            ],
        ),
        migrations.CreateModel(
            name='DukaanOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perms', models.TextField(default='READ SHOP')),
                ('dukaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.dukaan')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
