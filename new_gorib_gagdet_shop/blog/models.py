from django.db import models




class Blog(models.Model):
    image = models.ImageField(upload_to='blog/media/image')
    title = models.CharField(max_length=250)
    description = models.TextField()
    display = models.TextField()
    desgin = models.TextField()
    parformance = models.TextField()
    camera = models.TextField()
    Atlast  =  models.TextField()



STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]



class Reviewer(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(max_length=40,choices=STAR_CHOICES)

    def __str__(self):
        return self.name



class Benner(models.Model):
    image = models.ImageField(upload_to="blog/media/image")