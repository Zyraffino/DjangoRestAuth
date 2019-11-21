from django.db import models
from django.contrib.auth.models import User

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name

from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=144)
    description = models.CharField(max_length=144, blank=True)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)


class Snippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=144)

    snippet = models.TextField()
    highlighted = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'file_name': self.file_name} if self.file_name else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.snippet, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
        return '[{}] {}'.format(self.project.name, self.file_name)