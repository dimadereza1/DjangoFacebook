function openRegister() {
    $('#btn_redirect').click(function(){
        document.getElementById('reg_dialog').show();
    })
}

function closeRegister() {
    $('#close_btn').click(function(){
        document.getElementById('reg_dialog').close();
    })
}

function submData() {
    $('#top_form').submit(function(){
        $.ajax('/reg/', {
            'type':'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'data_username': $('#username_id').val(),
                'data_email': $('#id_email').val(),
                'data_password': $('#id_passwordd').val()
            }
        })
    }
    )
}

$(document).ready(function() {
    openRegister();
    closeRegister();
    submData();
})