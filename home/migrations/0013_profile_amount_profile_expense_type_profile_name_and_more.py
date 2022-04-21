# Generated by Django 4.0.3 on 2022-04-19 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_userdetails_alter_expense_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='expense_type',
            field=models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='income',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='userdetails',
        ),
    ]