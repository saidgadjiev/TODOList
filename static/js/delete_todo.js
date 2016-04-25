/**
 * Created by said on 25.04.16.
 */
$(document).ready(function () {
    $(document).on('click', "input[name='delete']", function () {
        var row = $(this).closest('tr');
        var $del = $(this);
        $.post('/delete-todo/', {
            'id': $del.data('id')
        }).done(function () {
            row.remove();
        });
    });
});
