# Generated by Django 4.0.3 on 2022-04-18 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userdetails_alter_expense_user_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='user',
            new_name='username',
        ),
    ]
