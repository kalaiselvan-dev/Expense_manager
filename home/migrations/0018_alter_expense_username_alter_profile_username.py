# Generated by Django 4.0.3 on 2022-04-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_expense_username_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
