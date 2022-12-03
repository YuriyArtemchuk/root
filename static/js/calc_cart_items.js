const calculate = () => {
    // 1
    let checkedCells = $('.check:checked');
    let totalPrice = 0;
    let selItemsList = '';

    // 2
    for (let cell of checkedCells) {
        let parentRow = $(cell).parent().parent();
        totalPrice += parseFloat($(parentRow).find('td.price_cell').text());
        selItemsList += $(parentRow).find('td.id_cell').text() + ',';
    }
    selItemsList += totalPrice;

    // 3
    console.log(`totalPrice = ${totalPrice}`);
    console.log(`selItemsList = ${selItemsList}`);
    $('#total').text(`${totalPrice.toFixed(2)} грн.`);
    $('#bill-btn').attr('href', `/orders/order/${selItemsList}`);
};

$(document).ready(() => {
    // 1
    console.log('calc_cart_items -> Start');
    calculate();

    // 2
    $('.check').click(() => {
        console.log('check -> Click');
        calculate();
    })
});
