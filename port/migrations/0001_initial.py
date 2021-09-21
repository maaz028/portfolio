# Generated by Django 3.2.5 on 2021-08-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('sample1', models.ImageField(default='', upload_to='port/images')),
                ('sample2', models.ImageField(default='', upload_to='port/images')),
            ],
        ),
    ]
