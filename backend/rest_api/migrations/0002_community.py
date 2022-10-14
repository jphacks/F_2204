# Generated by Django 4.1.2 on 2022-10-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('community_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Community ID')),
                ('community_name', models.CharField(max_length=255, verbose_name='Community Name')),
            ],
        ),
    ]
