# Generated by Django 3.2 on 2021-04-26 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0003_alter_status_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify', models.CharField(default=None, max_length=800)),
                ('nuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileupload.user_profile', unique=True)),
            ],
        ),
    ]
