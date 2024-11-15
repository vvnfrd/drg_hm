# Generated by Django 5.0.6 on 2024-07-08 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='превью')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='превью')),
                ('video_url', models.URLField(verbose_name='ссылка на видео')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='курс')),
            ],
        ),
    ]
