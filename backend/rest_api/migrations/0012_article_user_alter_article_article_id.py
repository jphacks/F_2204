# Generated by Django 4.1.2 on 2022-10-19 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0011_delete_user_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rest_api.user', verbose_name='記事を投稿するユーザID'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='記事のID'),
        ),
    ]
