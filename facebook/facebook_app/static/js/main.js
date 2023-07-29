function openEdits() {
    $('#edit_profilee').click(function(){
        document.getElementById('edit_profile_data').show();
        document.getElementById('bodyb').inert = true;
    })
}

function closeEdits() {
    $('#close_edits_btn').click(function(){
        document.getElementById('edit_profile_data').close();
        document.getElementById('bodyb').inert = false;
    })
}

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

// function openPost() {
//     document.getElementsByClassName('open_post').click(function(){
//         document.getElementById('post_dialogg').show();
//     })
// }

$(function(){
    $(document).click(function(event){
        open_post_btn = $(event.target);

        if(open_post_btn.attr('class') == 'open_post'){
            document.getElementById('post_dialogg').show();
        }
    })
})

$(function() {
    $(document).click(function(event) {
        delete_btn_id = $(event.target);

        if(delete_btn_id.attr('class') == 'delete_btnn'){
            console.log(delete_btn_id.data('id'));
            $.ajax('/profile/', {
                'type':'POST',
                'async': true, 
                'dataType': 'json',
                'data':{
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'delete_post': delete_btn_id.data('id')                
                },
                'success':function(data){
                    window.location.href = '/profile/'
                }
            })
        }   
    })
})

$(function() {
    $(document).click(function(event) {
        delete_btn_idd = $(event.target);

        if(delete_btn_idd.attr('class') == 'open_post'){
            console.log(delete_btn_idd.data('id'));
            $.ajax('/profile/', {
                'type':'POST',
                'async': true, 
                'dataType': 'json',
                'data':{
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'vw_post': delete_btn_idd.data('id')                
                },
                'success':function(data){
                    document.getElementById('post_photo').src = '/media/' + data['post_w_img']
                }
            })
        }   
    })
})



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
    $('#fbtn').click(function() {
        $.ajax('/create_post/', {
            'type':'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'data_post_text': $('#post_txt').val(),
            },
            'success': function(data){
                window.location.href = '/'
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

$(function(){
    $('#edit_profilee').click(function(){
        $.ajax('/profile/', {
            'type': 'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'cr_user':document.getElementById('username_o_us').innerText
            },
            'success':function(data){
                document.getElementById('username_inp').value = data['user_username'];
            }
        })
    })
})

$(function(){
    $('#id_ava').change(function(){
        let formData = new FormData();

        formData.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
        formData.append('file', document.getElementById('id_ava').files[0]);
        formData.append('ava', 0)
        console.log(document.getElementById('id_ava').files[0])

        $.ajax('/profile/', {
            'type': 'POST',
            'async': true, 
            'dataType': 'json',
            'data': formData,
            'processData': false,
            'contentType': false,
            'success': function(data){
                console.log(data['new_avatar'])
                document.getElementById('avatar_user_prof').src = data['new_avatar']
                document.getElementById('profile_cr_av').src = data['new_avatar']
            }
        })
    })
})

$(document).ready(function() {
    closeEdits();
    openEdits();
    submData();
    openRegister();
    closeRegister();
    LoadImg();
    GetDataPost();
    $('#file_upload').on('click', function(e) {
        e.preventDefault();
    $('#id_image').trigger('click');
    });
    $('#avatar_upload').on('click', function(e) {
        e.preventDefault();
    $('#id_ava').trigger('click');
    });
    $('#background_upload').on('click', function(e) {
        e.preventDefault();
    $('#id_bgg').trigger('click');
    });
})

