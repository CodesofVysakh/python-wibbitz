from django.db import models


BLOG_TYPE = [
    ("blog_post", "Blog Post"),
    ("webinar", "Webinar"),
    ("report", "Report"),
]

class Customer(models.Model):
    image = models.FileField(upload_to="Customer/")

    def __str__(self):
        return str(self.id)


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Feature(models.Model):
    image = models.ImageField(upload_to="Feature/images")
    icon = models.FileField(upload_to="Feature/icons")
    icon_background = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="Feature/logos")

    class Meta:
        db_table = "web_feature"
        ordering = ["-id"]

    def __str__(self):
        return self.title

class VideoBlog(models.Model):
    image = models.ImageField(upload_to="VideoBlog/images")
    title = models.CharField(max_length=255)
    logo = models.FileField(upload_to="VideoBlog/logos")
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    image = models.ImageField(upload_to="Testimonial/images")
    logo = models.FileField(upload_to="Testimonial/logos")
    name = models.CharField(max_length=255)
    description = models.TextField()
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    is_featured = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class MarketingFeature(models.Model):
    image = models.FileField(upload_to="MarketingFeature/images")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    image = models.ImageField(upload_to="Product/images")
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.FileField(upload_to="Product/logos")

    def __str__(self):
        return self.title

class Blog(models.Model):
    image = models.ImageField(upload_to="Blog/images")
    title = models.CharField(max_length=255)
    content_type = models.TextField(max_length=255, choices=BLOG_TYPE)
    title_redirection = models.CharField(max_length=255, default=True)

    def __str__(self):
        return self.title