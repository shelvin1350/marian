# Generated by Django 5.0.4 on 2024-05-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_alter_attendance_extrahours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Afternoon',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='ExtraHours',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Forenoon',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='TotalHours',
            field=models.FloatField(blank=True, null=True),
        ),
    ]