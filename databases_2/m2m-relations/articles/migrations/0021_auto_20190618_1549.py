# Generated by Django 2.1.1 on 2019-06-18 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_auto_20190618_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescope',
            options={'ordering': ['-is_main']},
        ),
    ]
