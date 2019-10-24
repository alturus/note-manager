import uuid

from django.conf import settings
from django.db import models


class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, default='')
    category = models.ForeignKey('categories.Category', related_name='notes', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_favorited = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ('-created', )

    def __str__(self):
        return self.title
