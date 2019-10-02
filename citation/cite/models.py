from django.db import models


class JournalCitation(models.Model):
    article_title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    journal_title = models.CharField(max_length=1000)
    journal_volume = models.IntegerField()
    journal_issue_number = models.IntegerField()
    doi = models.CharField(max_length=1000, unique=True)
    date_published = models.DateField(max_length=1000)
