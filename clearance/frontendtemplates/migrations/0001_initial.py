# Generated by Django 4.2.4 on 2023-08-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_1', models.TextField(blank=True, null=True)),
                ('form_08', models.TextField(blank=True, null=True)),
                ('form_09', models.TextField(blank=True, null=True)),
                ('form_12', models.TextField(blank=True, null=True)),
                ('form_13', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
