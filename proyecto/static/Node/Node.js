<!-- ******* Codigo de configuracion Union con Node.js * express.js *  socket.io *******-->
    <!--
        Dede de estar ejecutando el server de Node:
    -->
    <script src="http://127.0.0.1:9000/socket.io/socket.io.js"></script>
    <!-- ******* Codigo de configuracion Union con Node.js * express.js *  socket.io *******-->

var socket = io.connect('http://127.0.0.1:9000/');//Puente de conexion a el server


socket.on('messagesFront', function (data) {//Se recibe el mensaje a el server.
	    console.log(data);
	    socket.emit('NewConection', "Nueva Conexion");//Se envia el mensaje a el server de nueva conexion.
	  });

