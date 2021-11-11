# Generated by Django 3.2.9 on 2021-11-04 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='ссылка картинки')),
            ],
            options={
                'verbose_name': 'Задний фон',
                'verbose_name_plural': 'Задний фон',
                'db_table': 'Background',
            },
        ),
    ]
