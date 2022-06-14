# Generated by Django 4.0.4 on 2022-06-13 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TutorApp', '0004_remove_gigpackages_package_gigpackages_package'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codeeditor',
            name='student',
        ),
        migrations.RemoveField(
            model_name='codeeditor',
            name='teacher',
        ),
        migrations.CreateModel(
            name='OrderRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('files', models.BinaryField(blank=True, editable=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TutorApp.students')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TutorApp.teachers')),
            ],
        ),
    ]
