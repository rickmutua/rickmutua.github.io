# Generated by Django 2.0 on 2017-12-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('screenshots', models.ImageField(blank=True, upload_to='screenshots/')),
                ('about', models.TextField(blank=True)),
                ('tech_sheet', models.TextField(blank=True)),
                ('tech', models.TextField(blank=True)),
                ('resources', models.TextField(blank=True)),
                ('deployed_site', models.URLField(blank=True)),
                ('github_repo', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='rick.Tag'),
        ),
    ]
