# Generated by Django 3.0.8 on 2020-08-06 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20200802_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseadd',
            name='course',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='adds', to='courses.Course'),
        ),
    ]