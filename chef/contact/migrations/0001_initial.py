# Generated by Django 4.0.3 on 2022-03-28 09:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('text', ckeditor.fields.RichTextField()),
                ('mini_text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='icons/')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('message', models.TextField(max_length=5000)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='icons/')),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('alt', models.CharField(max_length=100)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_images', to='contact.about')),
            ],
        ),
    ]
