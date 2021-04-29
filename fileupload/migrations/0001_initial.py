# Generated by Django 3.2 on 2021-04-26 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kycid', models.CharField(max_length=200, unique=True)),
                ('fname', models.CharField(max_length=200)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('display_picture', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=None, max_length=200)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileupload.user_profile')),
            ],
        ),
        migrations.CreateModel(
            name='files_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filetype', models.CharField(max_length=200, unique=True)),
                ('filename', models.FileField(upload_to='uploads/')),
                ('fileid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileupload.user_profile')),
            ],
        ),
    ]