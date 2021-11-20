from django.contrib import admin
from web.models import Customer, Subscriber, Feature, Blog, VideoBlog, Testimonial, MarketingFeature, Product, Contact


admin.site.register(Customer)
admin.site.register(Subscriber)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id","title","testimonial_author","author_designation","description"]

admin.site.register(Feature, FeatureAdmin)

admin.site.register(Blog)
admin.site.register(VideoBlog)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id","name","is_featured"]

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(MarketingFeature)
admin.site.register(Product)
admin.site.register(Contact)



