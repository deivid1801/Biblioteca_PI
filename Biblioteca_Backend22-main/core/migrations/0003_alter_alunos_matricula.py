# Generated by Django 5.1.6 on 2025-02-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_emprestimos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='matricula',
            field=models.IntegerField(),
        ),
    ]
