# Generated by Django 4.2 on 2023-06-11 17:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b_data_crud', '0003_data_mahasiwa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(13), django.core.validators.MaxValueValidator(19)])),
                ('height', models.PositiveIntegerField(null=True)),
                ('sex', models.PositiveIntegerField(choices=[(0, 'Terlentang'), (1, 'Berdiri')], null=True)),
                ('predictions', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]