import json

from django.shortcuts import render
from django.http.response import HttpResponse

from web.models import Customer, Subscriber, Feature, Blog, MarketingFeature, Product, Testimonial, VideoBlog, Contact
from web.forms import ContactForm


def index(request):
    customers = Customer.objects.all()
    latest_customers = Customer.objects.all()[:4]
    features = Feature.objects.all()
    blogs = Blog.objects.all()
    marketingfeatures = MarketingFeature.objects.all()
    products = Product.objects.all()
    featured_testimonials = Testimonial.objects.filter(is_featured=True)[:2]
    non_featured_testimonials = Testimonial.objects.filter(is_featured=False)
    videoblogs = VideoBlog.objects.all()[:3]

    form = ContactForm()

    context = {
        "customers" : customers,
        "features" : features,
        "blogs" : blogs,
        "marketingfeatures" : marketingfeatures,
        "products" : products,
        "featured_testimonials" : featured_testimonials,
        "non_featured_testimonials" : non_featured_testimonials,
        "videoblogs" : videoblogs,
        "form" : form,
        "latest_customers" : latest_customers,
    }
    return render(request,"index.html", context=context)

def create_subscriber(request):
    email = request.POST.get("email")

    if email:

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
    else:
        response_data = {
                "status" : "error",
                "title" : "Blank email field.",
                "message" : "Please enter a valid email."
            }

    return HttpResponse(json.dumps(response_data), content_type="application/javascript")


def contact(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        form.save()
    # email = request.POST.get("email")
    # first_name = request.POST.get("first_name")
    # last_name = request.POST.get("last_name")
    # company = request.POST.get("company")
    # company_size = request.POST.get("company_size")
    # industry = request.POST.get("industry")
    # job_role = request.POST.get("job_role")
    # country = request.POST.get("country")
    # user_agreement = request.POST.get("user_agreement")


    # if not Contact.objects.filter(email=email).exists():

    #     Contact.objects.create(
    #         email=email,
    #         first_name=first_name,
    #         last_name=last_name,
    #         company=company,
    #         company_size=company_size,
    #         industry=industry,
    #         job_role=job_role,
    #         country=country,
    #         user_agreement=user_agreement,
    #     )

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