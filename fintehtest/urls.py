
from django.urls import path
from fintehtest.apps import FintehtestConfig
from fintehtest.views import get_id_on_template, get_stripe_session_id


app_name = FintehtestConfig.name

urlpatterns = [
    
    path('',  get_stripe_session_id, name='get_stripe_session_id'),
    path('item/<int:pk>', get_id_on_template, name='get_id_on_template'),
    # buy/{id}
]


