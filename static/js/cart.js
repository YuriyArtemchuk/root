$(document).ready(() => {
    console.log('cart.js -> OK');

    $('.products').on('click', '.add-to-cart-btn', (event) => {
        console.log('add-btn -> OK');
        //
        let mess = 'Для використання кошика ви можете обрати один із двох режімів:\n'
        mess += '1 - збереження кошика у базі даних\n   (буде доступно в усіх браузерах і всіх комп\'ютерах)\n';
        mess += '2 - збереження кошика у браузері користувача \n   (буде доступно тільки в цьому браузері)\n';
        mess += 'Підтвержуєте вибір більш надійного першого варіанту?'
        //
        if (confirm(mess)) {
            // 1. Збереження кошику у базі даних
            // =================================
            console.log('Збереження кошику у базі даних');
            const userId = $('#user_id').val();
            console.log('User-ID: ' + userId);
            //
            if (userId == 'None') {
                alert('Для збереження кошика у базі даних Ви повинні авторізуватись')
                }
            else {
                let productId = $(event.target).prev().val();
                console.log('productId ->' + productId);
                // Відправка AJAX-запиту на сервер для збереження товару у БД:
                $.ajax({
                    url: '/cart/ajax_cart',
                    data: `uid=${userId}&pid=${productId}`,
                    success: (response) => {
                        console.log('AJAX -> work: ' + response.mess);
                        console.log('UID: ' + response.uid);
                        console.log('PID: ' + response.pid);
                        //
                        $('#cart-count').text(response.count);
                        $('.cart-summary').find('h5').text(response.count + 'товарів вибрано')
                        $('.cart-summary').find('h4').text('ВАРТІСТЬ:' + response.amount +' грн')

                    }
                });
            }
        } else {
            // 2. Збереження кошику у браузері
            // =================================
            console.log('Збереження кошику у браузері');
        }

    });

});