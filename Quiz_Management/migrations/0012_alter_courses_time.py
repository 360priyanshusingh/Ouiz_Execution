# Generated by Django 4.1 on 2022-10-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz_Management', '0011_courses_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
