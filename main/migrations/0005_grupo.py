# Generated by Django 5.1.2 on 2024-11-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_categoria_alter_pyme_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='GRUPO',
            fields=[
                ('id_grupo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
    ]
