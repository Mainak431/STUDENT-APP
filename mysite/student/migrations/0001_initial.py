# Generated by Django 2.0.1 on 2018-01-26 12:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CourseID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('C_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('D_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('HOD', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('Name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('D_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department')),
            ],
        ),
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_marks', models.IntegerField()),
                ('Grade', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('EnrollmentID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Address', models.TextField()),
                ('Enrollment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department')),
            ],
        ),
        migrations.CreateModel(
            name='Subwise_marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marks', models.IntegerField()),
                ('C_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Course')),
                ('EnrollmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Post')),
            ],
        ),
        migrations.AddField(
            model_name='marks',
            name='EnrollmentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Post'),
        ),
        migrations.AddField(
            model_name='course',
            name='Instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.faculty'),
        ),
    ]
