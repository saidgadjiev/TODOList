/**
 * Created by said on 25.04.16.
 */
$(document).ready(function () {
    $("#formAddJob").validate({
        submitHandler: function (form) {
            $.post('/add-todo/', {
                'job': $("textarea[name='job']").val(),
                'deadline': $("input[name='deadline']").val()
            }).done(function (resp) {
                var class_name;
                if (resp.overdude) {
                    class_name = "todo_overdude";
                } else {
                    class_name ="todo_active";
                }
                var row = '<tr ' + class_name + '><td>' + resp.deadline + '</td><td>' +
                    resp.job_text + '</td><td><input type="checkbox" name="completed" ' +
                    'data-id="' + resp.todo_id + '"></td><td><input type="button" name="delete" value="Delete" ' +
                    'data-id="' + resp.todo_id + '"></td></tr>';
                $('#todo_table').find('tr').first().after(row);
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
            $("#formAddJob").submit();
        }
    })
});

/**/