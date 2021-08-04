from django.db import models
from django.utils import timezone
import os

#BLOGS 

class BlogPost(models.Model):
    author=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    image=models.ImageField(upload_to='blogMedia/')
    title=models.CharField(max_length=200)
    displayText=models.TextField()
    body=models.TextField()
    date=models.DateTimeField(default=timezone.now)

    def delete(self):
        self.image.storage.delete(str(self.image))
        super(BlogPost, self).delete()

    def __str__(self):
        return self.title+' | '+self.author

class BlogPostComment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved =models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.post.title)+' | '+str(self.author)+': '+str(self.comment)



#News

class New(models.Model):
    image=models.ImageField(upload_to='newsMedia')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    source = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()

    def delete(self):
        self.image.storage.delete(str(self.image))
        super(New, self).delete()


    def __str__(self):
        return str(self.title)+' | '+str(self.date)


#EVENT

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    bannerimage=models.ImageField(upload_to='eventMedia')
    image1=models.ImageField(upload_to='eventMedia', blank=True)
    image2=models.ImageField(upload_to='eventMedia', blank=True)
    image3 = models.ImageField(upload_to='eventMedia', blank=True)
    image4 = models.ImageField(upload_to='eventMedia', blank=True)
    body = models.TextField()

    def delete(self):
        self.bannerimage.storage.delete(str(self.bannerimage))
        self.image1.storage.delete(str(self.image1))
        self.image2.storage.delete(str(self.image2))
        self.image3.storage.delete(str(self.image3))
        self.image4.storage.delete(str(self.image4))
        super(Event, self).delete()

    def __str__(self):
        return str(self.name)

class BannerEvents(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200)
    image=models.ImageField(upload_to='eventMedia')
    date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()

    def __str__(self):
        return self.heading