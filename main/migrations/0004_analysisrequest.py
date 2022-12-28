# Generated by Django 3.2.8 on 2022-12-28 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_paciente_pacient'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('denied', models.BooleanField(default=False)),
                ('pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pacient')),
            ],
        ),
    ]