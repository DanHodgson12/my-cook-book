$(document).ready(function () {
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('select').formSelect();

    $('#add-ingredient').click(function() {
        let duplicateRow = $('#ingredients-table tbody tr:first').clone();
        duplicateRow.find('input, select').val('');
        duplicateRow.appendTo('#ingredients-table tbody')
    });

});