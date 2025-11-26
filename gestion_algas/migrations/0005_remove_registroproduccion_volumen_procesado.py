from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ("gestion_algas", "0004_auto_20251126_1026"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registroproduccion",
            name="volumen_procesado",
        ),
    ]
