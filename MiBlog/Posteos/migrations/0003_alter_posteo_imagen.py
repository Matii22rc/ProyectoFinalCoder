# Generated by Django 4.2.4 on 2023-09-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posteos', '0002_posteo_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='imagen',
            field=models.ImageField(upload_to='posteos/'),
        ),
    ]
