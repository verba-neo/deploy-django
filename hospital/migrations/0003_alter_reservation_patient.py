# Generated by Django 4.2.2 on 2023-06-26 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_patient_doctors_alter_reservation_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='hospital.patient'),
        ),
    ]