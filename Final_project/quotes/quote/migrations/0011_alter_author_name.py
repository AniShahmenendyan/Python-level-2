# Generated by Django 4.0.4 on 2022-05-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0010_alter_quote_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]