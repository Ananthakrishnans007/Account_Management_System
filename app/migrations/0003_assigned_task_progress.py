# Generated by Django 4.0.6 on 2022-08-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigned_task',
            name='Progress',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success')], default='Pending', max_length=150),
        ),
    ]
