import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Question(models.Model):
    # Field of characters for question
    question_text = models.CharField(max_length=200)
    # Timestamp for publication
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # Return a boolean true if question was posted in the last 24 hours
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # Foreign Key relationship to parent Question database object
    # Choice has a many to one relationship to Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Field of characters for answer
    choice_text = models.CharField(max_length=200)
    # Number of votes, should start at 0
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
