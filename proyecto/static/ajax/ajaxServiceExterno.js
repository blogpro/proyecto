//For doing AJAX post
function tipoCambio(){
    loading(true);

    var meses = [
      "Enero",
      "Febrero",
      "Marzo",
      "Abril",
      "Mayo",
      "Junio",
      "Julio",
      "Agosto","Septiembre","Octubre","Noviembre","Diciembre",
    ];


    $.ajax({
       url : 'http://admin.creaturviajes.com/ws/tipocambio/',
       type : "get",
         success : function(json) {
          loading(false);
          var cambio = JSON.parse(json);

          var libra = cambio[2].fields;
          var dollar = cambio[0].fields;
          var euro = cambio[1].fields;
          var fecha = cambio[0].fields.fecha_cambio;
          console.log(fecha);
          fecha = fecha.split('T');
          fecha = fecha[0].split('-');

          $('.tcFecha').html(meses[fecha[1]-1]+' '+fecha[2]);
          $('.tc').html(dollar.cambio+'&nbsp;&nbsp;&nbsp;'+euro.cambio);

         },
         error : function(xhr,errmsg,err) {
            loading(false);
            console.log(xhr.status);
         }
    });
}


