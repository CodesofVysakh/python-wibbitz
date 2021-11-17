from django.contrib import admin
from web.models import Customer, Subscriber, Feature, Blog, VideoBlog, Testimonial, MarketingFeature, Product


admin.site.register(Customer)
admin.site.register(Subscriber)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id","title","testimonial_author","author_designation","description"]

admin.site.register(Feature, FeatureAdmin)

admin.site.register(Blog)
admin.site.register(VideoBlog)
admin.site.register(Testimonial)
admin.site.register(MarketingFeature)
admin.site.register(Product)


