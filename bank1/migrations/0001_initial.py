# Generated by Django 3.2 on 2021-04-26 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fileupload', '0003_alter_status_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ipfsmapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipfsid', models.CharField(max_length=200)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileupload.user_profile')),
            ],
        ),
    ]
