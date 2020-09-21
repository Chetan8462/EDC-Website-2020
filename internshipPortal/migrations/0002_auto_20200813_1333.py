# Generated by Django 3.0.8 on 2020-08-13 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200813_1333'),
        ('internshipPortal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='startup',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='internships_created', to='user.StartupProfile'),
        ),
        migrations.AddField(
            model_name='internshipapplication',
            name='applied_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='intern', to='user.StudentProfile'),
        ),
        migrations.AddField(
            model_name='internshipapplication',
            name='internship',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='internship', to='internshipPortal.Internship'),
        ),
    ]