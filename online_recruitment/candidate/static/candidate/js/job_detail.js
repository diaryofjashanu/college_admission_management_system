$(document).ready(function(){
    $('#application-form').on('submit', function(e){
        e.preventDefault();
        var form={
            'job_id' : $('[name=job_id]').val(),
            'candidate_name' : $('[name=candidate_name]').val(),
            'candidate_email': $('[name=candidate_email]').val(),
            'candidate_resume_url': $('[name=candidate_resume_url]').val(),
            'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
        }
        console.log(form)

        fetch(application_link,{
            method: "POST",
            //header:"appication/json",
            body: JSON.stringify(form)
        }).then(response => response.json())
        .then(data => {
            if(data.success){
                alert("Your application have been recieved.")
            }
            else{
                alert('Application Failed: '+data.message)
            }
        })
        .catch(error =>{
            console.log("error : "+error)
        })
    })
})