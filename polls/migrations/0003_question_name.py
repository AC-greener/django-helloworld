# Generated by Django 3.1.3 on 2020-11-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201117_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(default='zhuzhu', max_length=200),
            preserve_default=False,
        ),
    ]