from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    pub_date = models.DateTimeField("data published")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Food, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("data published")

    def __str__(self):
        return self.body
