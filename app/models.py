from django.db import models
from django.utils import timezone
import os
#BLOGS 

class BlogPost(models.Model):
    author=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media')
    title=models.CharField(max_length=200)
    text=models.TextField()
    date=models.DateTimeField(default=timezone.now)

    def delete(self):
        self.image.storage.delete(str(self.image))
        super(BlogPost, self).delete()

    def __str__(self):
        return self.title+' | '+self.author

class BlogPostComment(models.Model):
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    comment=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    