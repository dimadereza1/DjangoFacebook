$(function() {
    $('#search_chat_f').keyup(function(){
        $.ajax('/chats/', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'input': $(this).val(),
        },
        'success': function(data){
            document.getElementById('resurt_and_chats').innerHTML = data;
        }
        })
    })}
)