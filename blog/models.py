from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    date = models.DateField()

    def __str__(self):
        return self.title