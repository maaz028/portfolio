# Generated by Django 3.2.5 on 2021-08-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0003_auto_20210827_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('query', models.TextField()),
            ],
        ),
    ]
