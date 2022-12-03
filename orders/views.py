from django.shortcuts import render
from django.core.mail import send_mail
from cart.models import CartItem


def order(request, sel_list: str):
    sel_list_str = sel_list.split(',')  # '1,3,24500' => ['1', '3', '24500']
    sel_list_num = [int(x) for x in sel_list_str]  # ['1', '3', '24500'] => [1, 3, 24500]
    id_list = sel_list_num[:-1]  # [1, 3, 24500] => [1, 3]
    total_price = sel_list_num[-1]  # [1, 3, 24500] => 24500
    #
    final_list = []
    for id in id_list:
        item = CartItem.objects.get(id=id)
        final_list.append({
            'product_name': item.product.name,
            'category_name': item.product.category.name,
            'product_price': item.product.price,
            'product_photo': item.product.photo
        })
    #
    return render(request, 'orders/order.html', {
        'page_title': 'Перегляд замовлення',
        'total_price': total_price,
        'final_list': final_list,
        'init_list': sel_list
    })


def confirm(request, init_list: str):
    if request.method == 'GET':
        return render(request, 'orders/confirm.html', {
            'page_title': "Підтвердження замовлення",
            'init_list': init_list
        })
    elif request.method == 'POST':
        email = request.POST['email']
        #
        sel_list_str = init_list.split(',')  # '1,3,24500' => ['1', '3', '24500']
        sel_list_num = [int(x) for x in sel_list_str]  # ['1', '3', '24500'] => [1, 3, 24500]
        id_list = sel_list_num[:-1]  # [1, 3, 24500] => [1, 3]
        total_price = sel_list_num[-1]  # [1, 3, 24500] => 24500
        info_list = []
        #
        for id in id_list:
            item = CartItem.objects.get(id=id)
            info_list.append({
                'product_name': item.product.name,
                'category_name': item.product.category.name,
                'product_price': item.product.price
            })
            #
        subject = 'Повідомлення про замовлення на сайті OnlineShop'
        body = """
                <h1>Повідомлення про замовлення на сайті OnlineShop</h1>
                <hr />
                <h2 style="color: purple">Ви підтвердили замовлення наступних товарів</h2>
                <h3>
                <ol>
            """
        #
        for item in info_list:
            body += f"""
                <li>
                     {item.get('product_name')} / 
                     {item.get('category_name')} -
                     {item.get('product_price')} грн
                 </li>
        """
        #
        body += f"""
            </ol>
            </h3>
            <hr />
            <h2>
                    Загальна сума до сплати:
                    <span style="color: red">
                        {total_price} грн
                    </span>
                </h2>
            """
        #
        success = send_mail(subject, '', 'OnlineShop', [email], fail_silently=False, html_message=body)
        if success:
            return render(request, 'orders/thanks.html', {
                'page_title': "Подяка за замовлення",
                'email': email
            })
        else:
            return render(request, 'orders/failed.html', {
                'page_title': "Помилка поштового відправлення",
            })

