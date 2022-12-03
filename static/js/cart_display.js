$(document).ready(() => {

    console.log('cart_display -> START');
    const userId = $('#user_id').val();
    console.log('User-ID: ' + userId);

    if (userId != 'None') {
        $.ajax({
        url: '/cart/ajax_cart_display',
        data: `uid=${userId}`,
        success: (response) => {
            console.log('AJAX -> work: ');
            $('#cart-count').text(response.count);
            $('.cart-summary').find('h5').text(response.count + 'товарів вибрано')
            $('.cart-summary').find('h4').text(' ВАРТІСТЬ:' + response.amount +' грн')
        }
    });
    }
});