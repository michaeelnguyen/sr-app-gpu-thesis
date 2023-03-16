# Generated by Django 4.1.7 on 2023-03-15 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gallery.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('image', models.ImageField(max_length=255, upload_to=gallery.models.get_user_directory_path)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('niqe', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('brisque', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SRPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to=gallery.models.get_user_directory_path)),
                ('model_chosen', models.TextField()),
                ('niqe', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('brisque', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('original_photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.photo')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
