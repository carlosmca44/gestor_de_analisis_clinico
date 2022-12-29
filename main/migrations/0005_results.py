# Generated by Django 3.2.8 on 2022-12-28 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_analysisrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=500)),
                ('idanalysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.analysisrequest')),
            ],
        ),
    ]