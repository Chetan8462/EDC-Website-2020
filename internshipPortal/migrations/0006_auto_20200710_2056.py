# Generated by Django 3.0.6 on 2020-07-10 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200707_1827'),
        ('internshipPortal', '0005_auto_20200710_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipapplication',
            name='applied_by',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='user.StudentProfile'),
        ),
    ]