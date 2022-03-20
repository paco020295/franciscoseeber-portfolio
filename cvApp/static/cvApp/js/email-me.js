$(document).ready(function(){
$("#emailForm").submit( function(e){
        e.preventDefault();
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        dataString = jQuery('form#emailForm').serialize();
        jQuery.ajax({
            type: "POST",
            url: "mail/",
            data: dataString,
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin',
            success: function(data)
            {
                alertify.success('Email succesfully sent');
            },
            error: function(xhr, ajaxOptions, thrownError)
            {
                alertify.error(xhr.responseText);
            }
        });
        return false;
    });
});
