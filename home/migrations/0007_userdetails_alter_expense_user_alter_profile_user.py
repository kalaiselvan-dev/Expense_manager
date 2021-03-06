# Generated by Django 4.0.3 on 2022-04-18 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_profile_password_remove_profile_password1'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('password1', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userdetails'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userdetails'),
        ),
    ]
