# Generated by Django 2.1 on 2019-04-06 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OCR_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]