# Generated by Django 4.0.4 on 2022-05-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0007_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]