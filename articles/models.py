from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# models can be created as classes.


class article(models.Model):
    title = models.CharField(default='Enter Article Title', max_length=80)
    description = models.CharField(
        default='Article Description', max_length=150)
    content = models.TextField(default='Article Detailed Explanation')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(default='None', max_length=50)
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-details', kwargs={'pk': self.pk})


class category(models.Model):
    title = models.CharField(default='Enter Category Name', max_length=80)
    description = models.CharField(
        default='Category Description', max_length=150)

    def __str__(self):
        return self.title
