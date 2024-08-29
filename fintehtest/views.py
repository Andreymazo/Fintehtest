from django.shortcuts import render
import requests
from django.urls import reverse
from config.settings import BASE_URL
from fintehtest.forms import StripIdForm
from fintehtest.models import Item
import stripe

def get_stripe_session_id(request):
    session_url = 'https://api.stripe.com/v1/checkout/sessions'
    stripe.api_key = 'sk_test_51PsjVH07pGox0kT4xVp7n7OAmqmork1Kv4DjUh8EkB2EGLZdKnsjp5CayOqgJZOtPUXwlGbKeqoLLVw8qP6pZxyr00dnLftcE4'
    header = {'Authorization': 'Bearer ' + f'{stripe.api_key}'}
    queryset = Item.objects.all()
    context = {"queryset":queryset}
       
    return render(request, "templates/fintehtest/first.html", context)


def get_id_on_template(request, **kwargs):
    pk = kwargs['pk']
    item_instance = Item.objects.all().get(id=pk)

    stripe.api_key = "sk_test_51PsjVH07pGox0kT4xVp7n7OAmqmork1Kv4DjUh8EkB2EGLZdKnsjp5CayOqgJZOtPUXwlGbKeqoLLVw8qP6pZxyr00dnLftcE4"
    session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                        
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": f"{item_instance.price}",
                        "product_data": {
                            "name": f"{item_instance.name}",
                            "description":f"{item_instance.description}",
                        },
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=BASE_URL+reverse('fintehtest:get_id_on_template', kwargs={'pk': pk}),#https://example.com/success
            cancel_url=BASE_URL+reverse('fintehtest:get_id_on_template', kwargs={'pk': pk}),
        )
    context = {'item_instance':item_instance,
               'session_id':session.id}
    return render(request, "templates/fintehtest/second.html", context)