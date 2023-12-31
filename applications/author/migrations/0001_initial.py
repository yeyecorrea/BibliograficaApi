# Generated by Django 4.2.3 on 2023-08-05 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('image', models.ImageField(upload_to=None, verbose_name='Imagen')),
                ('biografia', models.TextField(verbose_name='Biografia')),
            ],
            options={
                'verbose_name': 'Autor',
                'managed': True,
            },
        ),
    ]
