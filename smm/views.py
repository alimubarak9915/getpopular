from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import (
    SmmServices,
    Category,
    Orders,
    Wallet,
)


@login_required()
def home(request):
    orders_obj = Orders.objects.filter(user=request.user)
    try:
        wallet_obj = Wallet.objects.get(user=request.user)
    except Exception as e:
        wallet_obj = None

    context = {
        'title': 'Get Popular',
        'navbar': 'home',
        'orders_obj': orders_obj,
        'wallet_obj': wallet_obj,

    }
    return render(request, 'smm/index.html', context=context)


def services(request):
    smm_services = SmmServices.objects.all().order_by('-service_name')
    context = {
        'title': 'Services',
        'navbar': 'services',
        'smm_services': smm_services,
    }
    return render(request, 'smm/services.html', context=context)


@login_required()
def orders(request):
    orders_data = Orders.objects.filter(user_id=request.user.pk)
    category_data = Category.objects.all()
    smm_data = SmmServices.objects.all()

    context = {
        'title': 'Orders',
        'navbar': 'orders',
        'orders_data': orders_data,
        'category_data': category_data,
        'smm_data': smm_data,
    }
    return render(request, 'smm/orders.html', context=context)


@login_required()
def tutorials(request):
    context = {
        'title': 'Tutorials',
        'navbar': 'tutorials'
    }
    return render(request, 'smm/tutorials.html', context=context)


def ajax_services_query(request):
    if request.method == 'GET':
        category = request.GET.get('cat')
        smm_services = list(SmmServices.objects.filter(category__category_name__icontains=category).values())
        return JsonResponse({'data': smm_services})


def ajax_service_info(request):
    if request.method == 'GET':
        service = request.GET.get('ser')
        smm_services = list(SmmServices.objects.filter(service_name__icontains=service).values())
        return JsonResponse({'data': smm_services})


@login_required()
def create_order(request):
    if request.method != 'POST':
        return None
    category_obj = Category.objects.get(category_name=request.POST.get('category'))
    smm_service_obj = SmmServices.objects.get(service_name=request.POST.get('services'))
    order_obj = Orders.objects.create(
        user=request.user,
        category=category_obj,
        smm_service=smm_service_obj,
        quantity=request.POST.get('quantity'),
        amount=request.POST.get('payable_amount'),
        link=request.POST.get('link'),
        status='pending',
    )
    wallet_obj = Wallet.objects.get(user=request.user)
    wallet_obj.wallet_balance -= int(request.POST.get('payable_amount'))
    wallet_obj.save()

    return redirect('smm:orders')


def terms_conditions(request):
    context = {
        'title': 'Terms & Conditions',
        'navbar': 'terms',

    }
    return render(request, 'smm/terms_of_service.html', context)


def add_funds(request):
    if request.method == 'POST':
        pass
    return redirect('smm:home')
