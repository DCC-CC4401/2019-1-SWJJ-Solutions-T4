# Generated by Django 2.1.7 on 2019-05-11 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_auto_20190511_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_evaluador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('app_paterno', models.CharField(blank=True, max_length=200, null=True)),
                ('correo', models.EmailField(max_length=200)),
            ],
        ),
    ]