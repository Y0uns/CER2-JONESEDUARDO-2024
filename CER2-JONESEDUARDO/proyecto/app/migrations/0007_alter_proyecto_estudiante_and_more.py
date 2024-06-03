# Generated by Django 4.2.6 on 2024-06-03 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_rename_patrocinio_proyecto_patrocinio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='estudiante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectos_creados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='profesorPatrocinador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectos_patrocinados', to=settings.AUTH_USER_MODEL),
        ),
    ]
