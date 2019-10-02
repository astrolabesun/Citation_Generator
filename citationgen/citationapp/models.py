import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class CiteBookField(models.Model):
    book_cite_text = models.CharField(max_length=200)
    cite_date = models.DateTimeField('citation made:')

    def __str__(self):
        return self.book_cite_text

    def was_citation_recent(self):
        return self.cite_date >= timezone.now() - datetime.timedelta(days=1)
