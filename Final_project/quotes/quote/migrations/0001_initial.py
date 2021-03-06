# Generated by Django 4.0.4 on 2022-05-10 14:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'db_table': 'quotes',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('author', models.ManyToManyField(to='quote.author')),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='author',
            name='quote',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='quote.quote'),
        ),
    ]
