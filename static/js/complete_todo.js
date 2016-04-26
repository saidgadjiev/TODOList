/**
 * Created by said on 26.04.16.
 */
$(document).ready(function () {
    $(document).on('click', "input[type='checkbox']", function () {
        var row = $(this).closest('tr');
        var $del = $(this);
        $.post('/comlete-todo/', {
            'id': $del.data('id')
        }).done(function (resp) {
            if (resp.complete) {
                row.addClass("strikeout todo_complete");
            } else {
                row.removeClass("strikeout todo_complete");
                row.addClass("todo_active");
            }
        });
    })
});
