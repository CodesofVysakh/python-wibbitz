from django.db import models


BLOG_TYPE = (
    ("blog_post", "Blog Post"),
    ("webinar", "Webinar"),
    ("report", "Report"),
)

COMPANY_SIZE = (
    ("1", "1-10"),
    ("2", "11-50"),
    ("3", "51-200"),
    ("4", "201-500"),
)

INDUSTRY = (
    ("1", "Agriculture"),
    ("2", "Banking & Finance"),
    ("3", "Business Services & Softwares"),
)

JOB_ROLE = (
    ("1", "C-Suite"),
    ("2", "VIP"),
)

COUNTRY = (
    ("us", "United States"),
    ("al", "Albania"),
)

class Customer(models.Model):
    product = models.ForeignKey("web.Product", on_delete=models.CASCADE)
    image = models.FileField(upload_to="Customer/")
    white_logo = models.FileField(upload_to="Customer/", blank=True, null=True)

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
    logo = models.FileField(upload_to="Testimonial/logos", null=True)
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    designation = models.CharField(max_length=255,null=True)
    company_name = models.CharField(max_length=255,null=True)
    is_featured = models.BooleanField()

    class Meta:
        db_table = "web_testimonial"
        ordering = ["id"]

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
    hero_image = models.FileField(upload_to="Product/hero-images")
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    background_color = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.FileField(upload_to="Product/logos")

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField(upload_to="Blog/images")
    title = models.CharField(max_length=255)
    content_type = models.TextField(max_length=255, choices=BLOG_TYPE)
    title_redirection = models.CharField(max_length=255, default=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_size = models.CharField(max_length=255, choices=COMPANY_SIZE)
    industry = models.CharField(max_length=255, choices=INDUSTRY)
    job_role = models.CharField(max_length=255, choices=JOB_ROLE)
    country = models.CharField(max_length=255, choices=COUNTRY)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table = "web_contact"
        ordering = ["-id"]

    def __str__(self):
        return self.first_name


    
