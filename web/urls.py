from django.urls import path
from web.views import index, create_subscriber, contact


app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("subscribe/", create_subscriber, name="create_subscriber"),
    path("contact/", contact, name="contact")

]
