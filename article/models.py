from django.db import models
from Turttle.settings import MEDIA_ROOT
from .utils import *


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
    thumbnail = models.ImageField(
        default='media/article/article_default.jpeg', upload_to=article_media_wrapper)
    url = models.CharField(max_length=100)
    category = models.ForeignKey(Categroy, on_delete=models.CASCADE)

    def __str__(self):
        return '{}::{}'.format(self.title, self.description)
