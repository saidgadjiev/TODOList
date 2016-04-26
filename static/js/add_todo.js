/**
 * Created by said on 25.04.16.
 */
$(document).ready(function () {
    $("#form_add_job").validate({
        submitHandler: function (form) {
            $.post('/add-todo/', {
                'job': $("textarea[name='job']").val(),
                'deadline': $("input[name='deadline']").val()
            }).done(function (resp) {
                $('#todo_table').find('tr').first().after('<tr><td>' + resp.deadline + '</td><td>' +
                    resp.job_text + '</td><td><input type="checkbox" name="completed" ' +
                    'data-id="' + resp.todo_id + '"></td><td><input type="button" name="delete" value="Delete" ' +
                    'data-id="' + resp.todo_id + '"></td></tr>');
            });
            $(form).trigger('reset')
        },
        rules: {
            job: {required: true, minlength: 1},
            deadline: "required"
        },
        messages: {
            job: {
                required: "Please enter job text",
                minlength: "Please enter min 1 symb"
            },
            deadline: "Pick the date"
        }
    });
    $(document).keypress(function (event) {
        var key = event.which;
        if (key == 13) {
            event.preventDefault();
            console.log('Submit');
            $("#form_add_job").submit();
        }
    })
});

/**/