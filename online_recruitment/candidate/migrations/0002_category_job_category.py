# Generated by Django 5.1.6 on 2025-03-13 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='candidate.category'),
            preserve_default=False,
        ),
    ]
