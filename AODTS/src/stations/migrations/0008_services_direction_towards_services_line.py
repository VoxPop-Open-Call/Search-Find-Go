# Generated by Django 4.1.5 on 2023-02-10 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0007_ramproutes_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='direction_towards',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stations.stop'),
        ),
        migrations.AddField(
            model_name='services',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='platforms', to='stations.line'),
        ),
    ]
