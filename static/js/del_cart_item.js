$(document).ready(() => {

    console.log('del_cart_item -> Start');
    $('.del-btn').click((event) => {
        let delItemId = $(event.target).prev().val();
        $.ajax({
            url: '/cart/ajax_del_cart_item',
            data: `del_item_id=${delItemId}`,
            success: (response) => {
                alert(response.report);
                window.location = '/cart';
            }
        });
    });
});