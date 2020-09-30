# Generated by Django 3.0.6 on 2020-09-28 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=120)),
                ('publisher', models.CharField(max_length=100)),
                ('stock', models.IntegerField(max_length=100)),
            ],
        ),
    ]