# Generated by Django 5.1.2 on 2024-10-14 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pyme',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='resenna',
            name='pyme',
        ),
        migrations.RemoveField(
            model_name='reporte',
            name='pyme',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Resenna',
        ),
        migrations.DeleteModel(
            name='Pyme',
        ),
        migrations.DeleteModel(
            name='Reporte',
        ),
    ]