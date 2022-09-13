import stripe
import requests

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

from .models import Item


def buy_item(request, id):
    product = str(id)
    item = get_object_or_404(Item, pk=id)
    price = stripe.Price.search(
        api_key=settings.STRIPE_API_KEY, query="product:" + product
    )
    price_id = price["data"][0]["id"]
    session = stripe.checkout.Session.create(
        api_key=settings.STRIPE_API_KEY,
        success_url=settings.BASE_URL,
        cancel_url=settings.BASE_URL,
        mode="payment",
        payment_method_types=["card"],
        line_items=[{"price": price_id, "quantity": 1}],
    )
    return JsonResponse(
        {
            "session_id": session["id"],
            "item_id": item.id,
            "item_name": item.name,
            "item_description": item.description,
            "item_price": item.price,
        }
    )


@require_http_methods(["GET"])
def get_item(request, id):
    session = requests.get(f"{settings.BASE_URL}/buy/{id}/").json()
    return render(
        request,
        "payment/payment.html",
        {
            "session_id": session["session_id"],
            "item_id": session["item_id"],
            "item_name": session["item_name"],
            "item_description": session["item_description"],
            "item_price": session["item_price"],
            "api_key": settings.STRIPE_PUBLIC_KEY,
        },
    )
