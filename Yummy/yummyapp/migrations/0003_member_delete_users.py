# Generated by Django 4.2.7 on 2023-11-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummyapp', '0002_rename_employee_users_rename_phoneno_users_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
