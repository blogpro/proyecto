angular.module('factoryModule', [])

	.factory('NgToast',function (ngToast,$timeout) {
        return {
            msjToast: function (opciones) {
                var options = {
                    content: opciones.mensaje,
                    animation: 'slide',
                    horizontalPosition: 'right',
                    verticalPosition: 'top',
                    maxNumber: 0,
                    className: opciones.clase,
                    timeout: 5000
                };
                $timeout(function () {
                    ngToast.create(options);
                }, 400);
            }
        }
    })

    .factory('ServiceHTTP',function ($resource,$timeout) {
        var urlApi = "http://systab.herokuapp.com/",
            resource = "",
            resultado = "";
        return {
            query: function (url) {
                resource   = $resource(urlApi + url);
                resultado = resource.query();
                return resultado;
            },
            get: function (url,id) {
                resource   = $resource(urlApi + url+':id');
                resultado = resource.get({id:id});
                return resultado;
            },
            post: function (url,data) {
                resource   = $resource(urlApi + url);
                resultado = resource.save(data);   
                return resultado;
            },
            borrar: function (url,id) {
                resource   = $resource(urlApi + url+':id');
                resultado = resource.delete({id:id});   
                return resultado;
            },
            update: function (url,data) {
                resource   = $resource(urlApi + url);
                resultado = resource.update(data);   
                return resultado;
            }
        }
    })