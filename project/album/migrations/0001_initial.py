# Generated by Django 4.2 on 2023-07-09 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='album.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='tag',
            field=models.ManyToManyField(blank=True, to='album.tag'),
        ),
    ]
