# Generated by Django 3.2.9 on 2021-11-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('gender', models.TextField(default='M')),
                ('address', models.TextField(default='India')),
            ],
        ),
        migrations.CreateModel(
            name='SutdentDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('qualification', models.CharField(max_length=20)),
            ],
        ),
    ]
