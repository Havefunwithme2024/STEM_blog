from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
import stripe

from .models import Tariff, TemporarySave
from account.models import Profile

def tariff_plan_view(request):
    tarrifs = Tariff.objects.order_by('-pk')
    context = {
        'tariffs': tarrifs,
        'title':'Тарифы'
    }
    return render(request, 'payment/tariff_plan.html', context)

def pay_activate(request, pk_tariff):
    if request.user.is_authenticated:
        tariff = Tariff.objects.get(pk=pk_tariff)
        temporary_saving = TemporarySave.objects.create(customer=request.user,
                                                        tariff=tariff)
        temporary_saving.save()
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session_stripe = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data':{
                        'currency': 'USD',
                         'product_data': {
            'name': 'Тестовая оплата на сайте БЛОГ'
        },
                        'unit_amount': int(tariff.price * 100)
                    },
                    'quantity': 1
                }
            ],
            mode='payment', success_url=request.build_absolute_uri(reverse('success_page')),
            cancel_url=request.build_absolute_uri(reverse('cancel_page'))
        )
        return redirect(session_stripe.url, 303)
    else:
        return redirect(request.META.get('HTTP_REFERER', 'index_page'))


def success_view(request):
    if request.user.is_authenticated:
        user = request.user
        temporary_saving = TemporarySave.objects.get(customer=user)
        profile = Profile.objects.get(user=user)
        profile.tariff = temporary_saving.tariff
        profile.save()

        temporary_saving.delete()
        context = {
            'title': 'Конечная оплата'
        }
        return render(request, 'payment/success.html', context)
    else:
        return redirect(request.META.get('HTTP_REFERER', 'index_page'))

def cancel_view(request):
    if request.user.is_authenticated:
        user = request.user
        temporary_saving = TemporarySave.objects.get(customer=user)
        temporary_saving.delete()
        context = {
            'title': 'Неуспешная оплата'
        }
        return redirect(request, 'payment/cancel.html', context)
    else:
        return redirect(request.META.get('HTTP_REFERER', 'index_page'))









