# Generated by Django 4.2.1 on 2023-05-08 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Autores', '0001_initial'),
        ('Livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Autores.autor'),
            preserve_default=False,
        ),
    ]
