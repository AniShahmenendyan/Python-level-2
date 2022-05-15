# Generated by Django 4.0.4 on 2022-05-12 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quote', '0012_remove_quote_user_author_user_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='context_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
