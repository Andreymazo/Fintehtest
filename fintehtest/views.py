import json
from django.shortcuts import render
import requests
from django.urls import reverse
from config.settings import BASE_URL, STRIP_API_KEY
from fintehtest.forms import StripIdForm
from fintehtest.models import Item
import stripe
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from config import settings
"""Сначала надо зарегистрироваться https://dashboard.stripe.com/ станет доступен Апи ключ, передаем в джейсон"""
def get_stripe_session_key(request):
    # session_url = 'https://api.stripe.com/v1/checkout/sessions'
    # stripe.api_key = settings.STRIP_API_KEY# 'sk_test_51PsjVH07pGox0kT4xVp7n7OAmqmork1Kv4DjUh8EkB2EGLZdKnsjp5CayOqgJZOtPUXwlGbKeqoLLVw8qP6pZxyr00dnLftcE4'
    # header = {'Authorization': 'Bearer ' + f'{stripe.api_key}'}
    if request.method == "GET":
        queryset = Item.objects.all()
        context = {"queryset":queryset}
    
    # return render(request, "templates/fintehtest/first.html", context)
    
    return JsonResponse({"publicKey": settings.STRIPE_PUBLISHABLE_KEY})
# def get_session_id(request):
#     if request.method=="GET":
#         try:
#             checkout_session = stripe.checkout.Session.create(
#                     client_reference_id = request.user.id if request.user.is_authenticated else None,
#                     success_url=BASE_URL + "success?session_id={CHECKOUT_SESSION_ID}",
#                     cancel_url=BASE_URL + "cancel/",
#                     payment_method_types= ["card"],
#                     mode = "subscription",
#                     line_items=[
#                     {
                            
#                         "price_data": {
#                             "currency": "usd",
#                             "unit_amount": f"{item.price}",
#                             "product_data": {
#                                 "name": f"{item.name}",
#                                 "description":f"{item.description}",
#                             },
#                         },
#                         "quantity": 1,
#                     },
#                 ],
#             )
#             return JsonResponse({"sessionId": checkout_session["id"]})
#         except Exception as e:
#             return JsonResponse({"error": str(e)})


"""Кнопка на теплейте черерз Джанго формы выдает номер обджекта, session_id получаем из функции get_id_on_template, htlbhtrnbv """
def get_obj_buttn(request):
    qureyset = Item.objects.all()
    form = StripIdForm()
    item=qureyset.first()
    context = {
        "form":form,
        "item":item
    }
    if request.method == "POST":
        form = StripIdForm(request.POST)
        if form.is_valid():
            # print('1111111111111', request.POST['name'])
            pk = request.POST['name']
            # session_id = get_session_id(request, pk)._container[0].hex() - обратно из джейсона
            
            # print('session_id', session_id) # 
            item = Item.objects.get(id=pk)
            context={"form":form,
                     'session_id':get_session_id(request, pk).id,
                     'item':item}
            # line_items=[
            #     {
                        
            #         "price_data": {
            #             "currency": "usd",
            #             "unit_amount": f"{item.price}",
            #             "product_data": {
            #                 "name": f"{item.name}",
            #                 "description":f"{item.description}",
            #             },
            #         },
            #         "quantity": 1,
            #     },
            # ],
           
            return render(request, "templates/fintehtest/second.html", context)
        else:
            # print('2222222222222222', request.GET)
            form = StripIdForm()

    return render(request, "templates/fintehtest/second.html", context)


"""На входе номер обджекта, на выходе сессион id"""
def get_session_id(request, pk):#**kwargs):
    # pk = kwargs['pk']
    item_instance = Item.objects.all().get(id=pk)

    stripe.api_key = STRIP_API_KEY
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
            success_url=BASE_URL+reverse('fintehtest:success'),
            cancel_url=BASE_URL+reverse('fintehtest:cancel'),
            # success_url=BASE_URL+reverse('fintehtest:get_id_on_template', kwargs={'pk': pk}),#https://example.com/success
            # cancel_url=BASE_URL+reverse('fintehtest:get_id_on_template', kwargs={'pk': pk}),
        )
    return session
# JsonResponse({
#             'session_id': session.id
#         })
    # context = {'item_instance':item_instance,
    #            'session_id':session.id}
    # return render(request, "templates/fintehtest/second.html", context)


# https://tech.raturi.in/django-stripe-integration-fully-explained-example

# #home view
# def home(request):
#  return render(request,'checkout.html')

#success view
def success_strip(request):
    return render(request,'templates/fintehtest/success.html')

 #cancel view
def cancel_strip(request):
    return render(request,'templates/fintehtest/cancel.html')
# https://github.com/vadushkin/Stripe-shopping/blob/main/products/views.py
# acct_1PsjVH07pGox0kT4

# andrey_mazo@andreymazo:~/Downloads$ stripe login
# Your pairing code is: warm-dazzle-gusto-galore
# This pairing code verifies your authentication with Stripe.
# Press Enter to open the browser or visit https://dashboard.stripe.com/stripecli/confirm_auth?t=wCjSXp1oox1CllYoOQvB6RT6bqE0gute (^C to quit)
# > Done! The Stripe CLI is configured for your account with account id acct_1PsjVH07pGox0kT4

# Please note: this key will expire after 90 days, at which point you'll need to re-authenticate.
# andrey_mazo@andreymazo:~/Downloads$ 
@csrf_exempt
def webhook(request):
    endpoint_secret = ''
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
    )
    except ValueError as e:
 # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
 # Invalid signature
        return HttpResponse(status=400)

 # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)
# stripe listen --forward-to localhost:8000/webhooks/stripe/
# https://github.com/vadushkin/Stripe-shopping/blob/main/products/views.py

