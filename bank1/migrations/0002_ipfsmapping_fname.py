# Generated by Django 3.2 on 2021-04-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipfsmapping',
            name='fname',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]