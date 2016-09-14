//For doing AJAX post
function enviarComentario(){
    loading(true);

    var message = $('#message').val();
    var post = $('#post').val();

    console.log(message);
    console.log(post);
    $.ajax({
       url : '/service-comentarios-query/',
       type : "post",
       data : {
        message : message,
        post: post
       },
         success : function(json) {
          loading(false);
          $('#message').val('');
          Carga(post);
          console.log(json);
         },
         error : function(xhr,errmsg,err) {
            loading(false);
            console.log(xhr.status);
         }
    });
}




function Carga(post)
{
  //Creamos un objeto dependiendo del navegador
  var objeto;
  if (window.XMLHttpRequest)
  {
    //Mozilla, Safari, etc
    objeto = new XMLHttpRequest();
  }else if (window.ActiveXObject){
    //Nuestro querido IE
     try {
        objeto = new ActiveXObject("Msxml2.XMLHTTP");
      } catch (e) {
        try { //Version mas antigua
          objeto = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (e) {}
     }
  }
  if (!objeto)
  {
    alert("No ha sido posible crear un objeto de XMLHttpRequest");
  }
  //Cuando XMLHttpRequest cambie de estado, ejecutamos esta funcion
  objeto.onreadystatechange=function(){
    cargarobjeto(objeto,post)
  }
    objeto.open('GET', '/service-comentarios-query/'+post+'/', true) // indicamos con el método open la url a cargar de manera asíncrona
    objeto.send(null) // Enviamos los datos con el metodo send
}

function cargarobjeto(objeto, id)
{
  if (objeto.readyState == 4){
    loading(false);
    var json = JSON.parse(objeto.response);
    var string = "";
     for(obj in json){
      if(json[obj].activo == true){
        string +='<div class="contentComentario">'
                        +'<div class="avatarComent">'
                            +'<img src="/static/images/avatar-comentario.png" class="img-circle">'
                        +'</div>'

                        +'<div class="infoComent">'
                            +'<div class="filaprincipalComent">'
                                +'<div class="userComent">'
                                  + json[obj].first_name + " " + json[obj].last_name
                                +'</div>'
                                +'<div class="dataComent">'
                                  + json[obj].fechaJs +", "+ json[obj].horaJs
                                +'</div>'
                            +'</div>'
                            +'<div class="descripcionComent">'
                                + json[obj].descripcion
                            +'</div>'
                        +'</div>'
        +'</div>';
        }else{
          string +='<div class="contentComentario">'
                        +'<div class="avatarComent">'
                            +'<img src="/static/images/avatar-comentario.png" class="img-circle">'
                        +'</div>'

                        +'<div class="infoComent">'
                            +'<div class="filaprincipalComent">'
                                +'<div class="userComent">'
                                  + json[obj].first_name + " " + json[obj].last_name
                                +'</div>'
                                +'<div class="dataComent">'
                                  + json[obj].fechaJs +", "+ json[obj].horaJs
                                +'</div>'
                            +'</div>'
                            +'<div class="descripcionComent">'
                                + json[obj].descripcion
                            +'</div>'
                                +'<div class="aprobarComentario">'
                                    + json[obj].nota
                                +'</div>'
                        +'</div>'
        +'</div>';
        }
     }
     $('#comentarios').html(string); //nombre del slect donde se va a mostrar
  } //si se ha cargado completamente
    
    //document.getElementById(id).innerHTML=objeto.responseText
  else{ //en caso contrario, mostramos un gif simulando una precarga
      loading(true);
  }
}