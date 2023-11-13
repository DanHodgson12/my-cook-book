$(document).ready(function () {
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('select').formSelect();

    $('#ingredients-table tbody tr:first #delete-ingredient').hide();
    $('#add-ingredient').click(function() {
        let duplicateRow = $('#ingredients-table tbody tr:first').clone();
        duplicateRow.find('input, select').val('');
        duplicateRow.find('#delete-ingredient').show();
        duplicateRow.appendTo('#ingredients-table tbody');
    });
    $('#ingredients-table tbody').on('click', '#delete-ingredient', function() {
        $(this).closest('tr').remove();
    });

    $('#method-table tbody tr:first #delete-step').hide();
    $('#add-step').click(function () {
        let duplicateRow = $('#method-table tbody tr:first').clone();
        duplicateRow.find('input, select').val('');
        duplicateRow.find('#delete-step').show();
        duplicateRow.appendTo('#method-table tbody');
    });
    $('#method-table tbody').on('click', '#delete-step', function () {
        $(this).closest('tr').remove();
    });

    

});