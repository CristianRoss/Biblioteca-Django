# Generated by Django 4.2.1 on 2023-05-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('paginas', models.IntegerField()),
                ('editora', models.CharField(max_length=50)),
                ('edicao', models.IntegerField()),
                ('ano_publicacao', models.IntegerField()),
                ('idioma', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=20)),
            ],
        ),
    ]
