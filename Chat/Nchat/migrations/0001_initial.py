# Generated by Django 4.2.3 on 2023-07-25 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('timetamp', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nchat.group')),
            ],
        ),
    ]