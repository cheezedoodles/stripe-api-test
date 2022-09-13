from django.urls import path, include
from payment import views

app_name = "payment"

urlpatterns = [
    path("buy/<int:id>/", views.buy_item, name="buy_item"),
    path("item/<int:id>/", views.get_item, name="get_item"),
]
