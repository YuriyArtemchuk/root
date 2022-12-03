from django.shortcuts import render
from django.http import JsonResponse
from .models import CartItem


def index(request):
    return render(request, 'cart/index.html', {
        'page_title': 'Управління кошиком',
        'user_items': CartItem.objects.filter(user_id=request.user.id)
    })


def ajax_cart(request):
    response = dict()
    response['mess'] = 'I am server'
    uid = request.GET['uid']
    pid = request.GET['pid']
    response['uid'] = uid
    response['pid'] = pid

    CartItem.objects.create(
        user_id=uid,
        product_id=pid,
        status='Очікування замовлення'
    )
    response['report'] = 'Товар успішно збережений у кошику'
    #
    user_items = CartItem.objects.filter(user_id=uid)
    amount = 0.0
    for item in user_items:
        amount += item.product.price

    #
    response['count'] = len(user_items)
    response['amount'] = amount
    return JsonResponse(response)


def ajax_cart_display(request):
    uid = request.GET['uid']
    user_items = CartItem.objects.filter(user_id=uid)
    amount = 0.0
    for item in user_items:
        amount += item.product.price
    return JsonResponse({
        'amount': amount,
        'count': len(user_items)
    })


def ajax_del_cart_item(request):
    del_item_id = request.GET['del_item_id']
    del_item = CartItem.objects.get(id=del_item_id)
    del_item.delete()
    return JsonResponse({
        'report': f"Товар із ID: {del_item_id} був видалений із кошика!"
    })


