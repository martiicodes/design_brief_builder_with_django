# Generated by Django 4.2.14 on 2024-08-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignBrief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('project_description', models.TextField()),
                ('objectives', models.TextField()),
                ('target_audience', models.TextField()),
                ('competitors', models.TextField()),
                ('deliverables', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deadline', models.DateField()),
            ],
        ),
    ]
