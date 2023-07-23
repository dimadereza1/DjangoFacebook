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

function GetDataPost() {
    $('#fop').submit(function() {
        $.ajax('/create_post/', {
            'type':'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'data_post_text': $('#post_txt').val(),
            }
        })
    })
}


function LoadImg() {
    $('#id_image').change(function() {
        let formData = new FormData();

        formData.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
        formData.append('file', document.getElementById('id_image').files[0]);
        
        $.ajax('/create_post/', {
            'type': 'POST',
            'async': true, 
            'dataType': 'json',
            'data': formData,
            'processData': false,
            'contentType': false,
            'success': function(data){
                document.getElementById('cob').innerHTML = '<img src="/media/post/upload.png" style="margin: auto; width: 972px; height: 600px; border-radius: 5px;">'
            }
        })
    })
}

$(document).ready(function() {
    LoadImg();
    openRegister();
    closeRegister();
    submData();
    GetDataPost();
    $('#file_upload').on('click', function(e) {
        e.preventDefault();
    $('#id_image').trigger('click');
    });
})