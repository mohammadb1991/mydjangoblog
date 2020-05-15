from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length = 100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    # in add thumbnail
    # in add author
    def __str__(self):
        return self.title

    def sss(self):
        return self.body[0:50] + ' ....'    
