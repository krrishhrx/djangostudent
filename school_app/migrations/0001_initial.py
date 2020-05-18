# Generated by Django 3.0.6 on 2020-05-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_rollno', models.IntegerField(max_length=3)),
                ('student_name', models.CharField(max_length=30)),
                ('student_class', models.CharField(max_length=10)),
                ('student_guardian', models.CharField(max_length=30)),
                ('teacher_in_charge', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
