//For doing AJAX post

function enviarComentario(){
    console.log("Paso");
}




//When submit is clicked
 $("#submit").click(function(e) {
    console.log("Paso");

//Prevent default submit. Must for Ajax post.Beginner's pit.
 e.preventDefault();

//Prepare csrf token
 var csrftoken = getCookie('csrftoken');


//Collect data from fields
 var email = $('#inputEmail').val();
 var password = $('#inputPassword').val();

//This is the Ajax post.Observe carefully. It is nothing but details of where_to_post,what_to_post
//Send data  
 $.ajax({
       url : window.location.href, // the endpoint,commonly same url
       type : "POST", // http method
       data : { csrfmiddlewaretoken : csrftoken, 
       email : email,
       password : password
         }, // data sent with the post request

         // handle a successful response
         success : function(json) {
         console.log(json); // another sanity check
         //On success show the data posted to server as a message
         alert('Hi   '+json['email'] +'!.' + '  You have entered password:'+ json['password']);
         },

         // handle a non-successful response
         error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
         }
         });
});