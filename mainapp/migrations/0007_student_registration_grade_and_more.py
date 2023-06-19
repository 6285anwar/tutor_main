# Generated by Django 4.2.2 on 2023-06-19 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_student_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_registration',
            name='grade',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='institution',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='p_city',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='p_email',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='p_name',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='p_phone',
            field=models.CharField(max_length=240, null=True),
        ),
    ]