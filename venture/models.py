from django.db import models

# Create your models here.
class Slider(models.Model):
    slider_title = models.CharField(max_length=100)
    slider_desc = models.TextField()
    slider_btn = models.CharField(max_length=50)
    slider_image = models.ImageField(upload_to="slides/", default="slides/default.png")

    def __str__(self):
        return self.slider_title

class Quote(models.Model):
    quote_title = models.CharField(max_length=100)
    quote_desc = models.TextField()
    quote_head = models.CharField(max_length=50, default="Quote")
    quote_sub = models.CharField(max_length=50, default="Quote")

    def __str__(self):
        return self.quote_title

class Construction(models.Model):
    construction_head = models.CharField(max_length=100)
    construction_sub = models.CharField(max_length=50)
    construction_title= models.CharField(max_length=100)
    construction_image= models.ImageField(upload_to="constructions/")
    construction_desc = models.TextField()

    def __str__(self):
        return self.construction_head

class Testimonial(models.Model):
    testimonial_head = models.CharField(max_length=100)
    testimonial_sub = models.CharField(max_length=100)
    testimonial_name = models.CharField(max_length=50)
    testimonial_occ = models.CharField(max_length=50)
    testimonial_message = models.TextField()

    def __str__(self):
        return self.testimonial_head



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return {self.name}

