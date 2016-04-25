/**
 * Created by said on 25.04.16.
 */

$("input[name='completed']").click(function () {
    var $like = $(this);
    console.log('Completed' + $like.data('id'))
})
