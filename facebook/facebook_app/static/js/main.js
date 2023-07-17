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

$(document).ready(function() {
    openRegister();
    closeRegister();
})