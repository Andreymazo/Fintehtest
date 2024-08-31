
from django.urls import path
from fintehtest.apps import FintehtestConfig
from fintehtest.views import cancel_strip, get_obj_buttn, get_session_id, get_stripe_session_key, success_strip, webhook


app_name = FintehtestConfig.name

urlpatterns = [
    path('',  get_obj_buttn, name='get_obj_buttn'),
    path('get_stripe_session_key',  get_stripe_session_key, name='get_stripe_session_key'),
    path('item/<int:pk>', get_session_id, name='get_session_id'),
    # path('get_obj_buttn',  get_stripe_session_id, name='get_stripe_session_id'),
    path('success.html/', success_strip,name='success'),
    path('cancel.html/', cancel_strip,name='cancel'),
    path('webhooks/stripe/', webhook,name='webhook')
    # buy/{id}
]


