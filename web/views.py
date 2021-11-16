import json

from django.shortcuts import render
from django.http.response import HttpResponse

from web.models import Customer, Subscriber


def index(request):
    customers = Customer.objects.all()

    context = {
        "customers" : customers,
    }
    return render(request,"index.html", context=context)

def create_subscriber(request):
    email = request.POST.get("email")

    if not Subscriber.objects.filter(email=email).exists():

        Subscriber.objects.create(
            email=email
        )

        response_data = {
            "status" : "success",
            "title" : "Successfully Registered.",
            "message" : "You subscribed to our newsletter successfully."
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You are already Subscribed.",
            "message" : "You are already a member. No need to register again."
        }

    return HttpResponse(json.dumps(response_data), content_type="application/javascript")