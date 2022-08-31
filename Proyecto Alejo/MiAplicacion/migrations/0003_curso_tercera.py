# Generated by Django 4.0.6 on 2022-07-31 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiAplicacion', '0002_pariente_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('camada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tercera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datochar', models.CharField(max_length=40)),
                ('datoint', models.IntegerField()),
                ('datofecha', models.DateField()),
            ],
        ),
    ]