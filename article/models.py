from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

from Turttle.settings import MEDIA_ROOT
from PIL import Image
from .utils import PathAndRename
import sys
import os
from io import BytesIO


# Create your models here.
class Categroy(models.Model):
    name = models.CharField(max_length=144)
    description = models.CharField(max_length=144, blank=True)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}::{}'.format(self.name, self.description)


article_media_path = os.path.join(MEDIA_ROOT, 'article')
article_media_wrapper = PathAndRename(article_media_path)


class Article(models.Model):
    title = models.CharField(max_length=144)
    description = models.CharField(max_length=144, blank=True)
    pub_date = models.DateField(auto_now_add=True)
    origin_site = models.CharField(max_length=144, blank=True)
    thumbnail = models.ImageField(
        default='media/article/article_default.jpeg', upload_to=article_media_wrapper)
    url = models.CharField(max_length=100)
    category = models.ForeignKey(Categroy, on_delete=models.CASCADE)

    def __str__(self):
        return '{}::{}'.format(self.title, self.description)

    def save(self):
        im = Image.open(self.thumbnail)
        output = BytesIO()
        im = im.resize((100, 100))
        im.save(output, format='JPEG', quality=100)

        output.seek(0)
        self.thumbnail = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.thumbnail.name.split(
            '.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(Article, self).save()
