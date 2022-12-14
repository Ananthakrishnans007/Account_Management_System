# Generated by Django 4.0.6 on 2022-08-13 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_name', models.CharField(max_length=100)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=10)),
                ('DOB', models.DateField()),
                ('Category_Name', models.CharField(choices=[('Trainee', 'Trainee'), ('Trainer', 'Trainer'), ('Employee', 'Employee'), ('Staff', 'Staff')], default='Trainee', max_length=150)),
                ('State', models.CharField(max_length=50)),
                ('Postcode', models.IntegerField()),
                ('City', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField()),
                ('Image', models.ImageField(null=True, upload_to='Profile_pic')),
                ('Plus_two', models.ImageField(null=True, upload_to='Plus_two')),
                ('Degree', models.ImageField(null=True, upload_to='Degree')),
                ('Pg', models.ImageField(null=True, upload_to='Pg')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assigned_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=255)),
                ('File', models.FileField(null=True, upload_to='Task')),
                ('Submition_Date', models.DateField(auto_now_add=True)),
                ('Task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
