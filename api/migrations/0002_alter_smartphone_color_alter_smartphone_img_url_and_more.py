# Generated by Django 4.1.7 on 2023-03-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='img_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='memory',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='model',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='ram',
            field=models.CharField(max_length=20),
        ),
    ]
