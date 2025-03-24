$(document).ready(function () {
    $('#register-form').on('submit', function(e) {
        e.preventDefault();
        var form = {
            'name' : $('[name=name]').val(),
            'email' : $('[name=email]').val(),
            'url' : $('[name=url]').val(),
            'gender' : $('[name=gender]').val(),
            'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
        }
        console.log(form)

        $.ajax({
            url: 'http://127.0.0.1:8000/registration_form',
            type: 'POST',
            data: form,
            cache: false,
            success: function(response){
                if (response.success){
                    console.log('success')
                }
                else {
                    console.log('failed')
                }
            }
        })
    })
})