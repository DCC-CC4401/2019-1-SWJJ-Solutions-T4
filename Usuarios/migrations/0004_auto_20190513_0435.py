# Generated by Django 2.2 on 2019-05-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_auto_20190511_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntaje',
            name='puntaje',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]