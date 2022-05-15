# class OwnedModel(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL,
#     on_delete=models.CASCADE)
#
#     class Meta:
#         abstract = True
#
# class Belonging(OwnedModel):
#     name = models.CharField(max_length=100)
#
