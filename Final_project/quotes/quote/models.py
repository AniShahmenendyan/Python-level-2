from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.timezone import now


class CreateUpdateMixin(models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True





class Author(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True, default=None)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='context_users')



    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')


    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name

class Quote(CreateUpdateMixin):
    text = models.TextField(null=False, unique=True)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, default='', on_delete=models.CASCADE)


    class Meta:
        db_table = 'quotes'