$.ajaxSetup({
    headers: { "X-CSRFToken": "{{ csrf_token }}" }
});


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

function closePostsV(){
    document.getElementById('post_dialoggg').close();
    document.getElementById('bodyb').inert = false;
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

function closeChatV(){
    document.getElementById('chat_dialogg').close();
}
function sentMess(){

        let btn = $('#sent_mess_btn');
        console.log(btn.data('id'))
        $.ajax(btn.data('url'), {
            'type':'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'id_chat_data': btn.data('id'),
                'text_chat_f': document.getElementById('input_emess').value
            },
           'success':function(data){
                document.getElementById('chat_block').innerHTML += data;
                document.getElementById('if_n').outerText = none;
            }
        })
    }



$(function(){
    $('#not_coment_on_post_btn').click(function(){
        let btn = $(this);
        console.log(btn.data('id'))
        $.ajax(btn.data('url'), {
            'type':'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'delete_data_id': btn.data('id')
            },
           'success':function(data){
                document.getElementById('not_coment_on_post_btn').outerHTML = '<button data-id="{{a_p.0.id}}" data-url="/" class="likes_button" id="like_btn" style="background-color: white; border: none; margin-left: 80px;"><i id="ico_loke" data-visualcompletion="css-img" class="x1b0d499 x1d69dk1" style="background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/yN/r/fSIH5kPU1qz.png&quot;); background-position: 0px -180px; background-size: 26px 556px; width: 18px; height: 18px; background-repeat: no-repeat; display: inline-block;"></i> Подобається</button>';
                document.getElementById('nomber_of_like').innerHTML = Number(document.getElementById('nomber_of_like').innerHTML) - 1;
            }
        })
    })
})

$(function(){
    $('#inp_txt').keyup(function(){
        let btn = $(this);
        document.getElementById('search_data').show();
        $.ajax('/', {
            'type':'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'data_search': btn.val()
            },
           'success':function(data){
                document.getElementById('search_data').innerHTML = data;
            }
        })
    })
})

$(function(){
    $(document).click(function(event){
        var like = $(event.target);

        if(like.attr('class') == 'not_coment_on_post_btn'){
             
            $.ajax(like.data('url'), {
                'type':'POST',
                'async': true, 
                'dataType': 'json',
                'data':{
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'like': like.data('id'),
                    'is_liked': like.data('liked')
                },
                'success': function(data){
                    let elements = document.getElementsByClassName('like_btn');
                    for (let i=0; i < elements.length; i++) {
                        if (elements.item(i).getAttribute('data-id') == data['id_o_ppost']) {
                            if (data['is_liked'] == 1){
                                elements.item(i).innerHTML = `<button data-id="${data['id_o_ppost']}" data-liked="1" data-url="/" class="not_coment_on_post_btn" style="background-color: white; border: none; margin-left: 80px;"><i data-visualcompletion="css-img" class="x1b0d499 xi3auck" style="background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/yQ/r/YfS72vr1mwv.png&quot;); background-position: 0px -160px; background-size: 26px 502px; width: 18px; height: 18px; background-repeat: no-repeat; display: inline-block;"></i> Подобається</button>`;
                            } else {
                                elements.item(i).innerHTML = `<button data-id="${data['id_o_ppost']}" data-liked="0" data-url="/" class="not_coment_on_post_btn" style="background-color: white; border: none; margin-left: 80px;"><i data-visualcompletion="css-img" class="x1b0d499 x1d69dk1" style="background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yQ/r/YfS72vr1mwv.png);background-position:0 -180px;background-size:26px 502px;width:18px;height:18px;background-repeat:no-repeat;display:inline-block"></i> Подобається</button>`;
                            }
                        }
                    }
                    elements = document.getElementsByClassName('number_of_like');
                    for (let i=0; i < elements.length; i++) {
                        if (elements.item(i).getAttribute('data-id') == data['id_o_ppost']) {
                            elements.item(i).innerHTML = data['amount'];
                        }
                    }
                }
            })
        }
    })
})



function addComment(id){
        console.log('asdasd')
        $.ajax('/profile/', {
            'type':'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'form_dataa': $('#data_from_comment_form').val(),
                'data_forma_id': id
            },
            'success':function(data){
                document.getElementById('all_comments_here').innerHTML += data
            }
        })
    }



$(function(){
    $('#follower_btn').click(function(){
        let btn = $(this);
        $.ajax(btn.data('url'), {
            'type':'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'friend':true
            },
            'success':function(data){
                document.getElementById('follower_btn').outerHTML = '<button data-url="/view_profile/{{user_data.id}}/" id="unfollower_btn">Перестати дружити</button>';
            }
        })
    })
})

$(function(){
    $('#unfollower_btn').click(function(){
        let btn = $(this);
        $.ajax(btn.data('url'), {
            'type':'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'ofriend':true
            },
            'success':function(data){
                document.getElementById('unfollower_btn').outerHTML = '<button data-url="/view_profile/{{user_data.id}}/" id="follower_btn">Дружити</button>';
            }
        })
    })
})

$(function(){
    $(document).click(function(event){
        open_chat_btn = $(event.target);

        if(open_chat_btn.attr('class') == 'open_chat'){
            console.log('topq');
            document.getElementById('chat_dialogg').show();
            console.log('topw');

             
            $.ajax(open_chat_btn.data('url'), {
                'type':'POST',
                'async': true, 
                'dataType': 'json',
                'data':{
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'id_open_chat': open_chat_btn.data('id'),
                    'user_two': open_chat_btn.data('us')
                },
                'success':function(data){
                    document.getElementById('chat_dialogg').innerHTML = data;
                }
            })
        }
    })
})




$(function(){
    $(document).click(function(event){
        open_post_btn = $(event.target);

        if(open_post_btn.attr('class') == 'open_postt'){
            document.getElementById('post_dialoggg').show();
            document.getElementById('bodyb').inert = true;
             
            $.ajax(open_post_btn.data('url'), {
                'type':'POST',
                'async': true, 
                'dataType': 'json',
                'data':{
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'id_o_post_i_d': open_post_btn.data('id')
                },
                'success':function(data){
                    document.getElementById('post_dialoggg').innerHTML = data
                }
            })
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
    $('#edit_username_dataaaa').click(function(){
        $.ajax('/profile/', {
            'type': 'POST',
            'async': true, 
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'data_edit_username': document.getElementById('username_inp').value
            },
            'success':function(data){
                document.getElementById('username_o_us').innerText = data['new_username'];
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

$(function(){
    $('#id_backgroundd').change(function(){
        let formData = new FormData();

        formData.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
        formData.append('file', document.getElementById('id_backgroundd').files[0]);
        formData.append('backgg', 0)
        console.log(document.getElementById('id_backgroundd').files[0])

        $.ajax('/profile/', {
            'type': 'POST',
            'async': true, 
            'dataType': 'json',
            'data': formData,
            'processData': false,
            'contentType': false,
            'success': function(data){
                console.log(data['new_avatar'])
                document.getElementById('profile_cr_bg').src = data['new_background']
                document.getElementById('background_user_prof').src = data['new_background']
            }
        })
    })  
})

function closeSearchData() {
    document.getElementById('search_data').close();
}


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
    $('#id_backgroundd').trigger('click');
    });
})

// $(document).ready(function() {
//     $.ajax('/', {
//         'type': 'POST',
//         'async': true, 
//         'dataType': 'json',
//         'data': {
//             'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
//             'for_posts': true
//         },
//         'success': function(data){
//             document.getElementById('div_for_all_posts').innerHTML = data
//         }
//     })
// }
// )
