# Generated by Django 2.0.13 on 2020-09-04 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_project_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='section',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='resume.Section'),
            preserve_default=False,
        ),
    ]
