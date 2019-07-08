from django.db import models

class Tag(models.Model):
    name = models.CharField(blank=False, null=False, max_length=15)
    text = models.TextField(blank=True, max_length=100)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(blank=False, null=False, max_length=15)
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    subtitle = models.TextField(blank=True, max_length=1000)
    text = models.TextField(blank=True, max_length=10000)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
