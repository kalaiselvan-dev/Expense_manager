# Generated by Django 4.0.3 on 2022-04-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_user_userdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]