# Generated by Django 2.1.1 on 2019-06-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20190617_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
        migrations.AddField(
            model_name='scope',
            name='article',
            field=models.ManyToManyField(related_name='scopes', through='articles.ArticleScope', to='articles.Article'),
        ),
    ]