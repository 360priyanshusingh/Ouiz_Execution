# Generated by Django 4.1 on 2022-10-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz_Management', '0012_alter_courses_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]