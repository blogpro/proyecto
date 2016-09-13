//For doing AJAX post
function enviarComentario(){
    loading(true);

    var message = $('#message').val();
    var post = $('#post').val();

    console.log(message);
    console.log(post);
    $.ajax({
       url : '/service-comentarios-query/', // the endpoint,commonly same url
       type : "post", // http method
       data : {
        message : message,
        post: post
       },
         success : function(json) {
          loading(false);
          
          $('#message').val('');
          console.log(json);
         },
         error : function(xhr,errmsg,err) {
            loading(false);
            console.log(xhr.status); // provide a bit more info about the error to the console
         }
         });
}