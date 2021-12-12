from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class comments(models.Model):
    articleA = models.ForeignKey(
        article, on_delete=models.CASCADE, related_name='comments',)
    msg = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.msg

    def get_absolute_url(self):
        return reverse('articleview')
