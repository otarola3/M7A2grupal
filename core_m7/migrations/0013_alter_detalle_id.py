# Generated by Django 4.2.1 on 2023-05-31 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_m7', '0012_detalle_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
