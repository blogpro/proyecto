angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            query: function (servicio) {
            	var urlApi = "http://systab.herokuapp.com/";
                var resource   = $resource(urlApi + servicio),
                	resultado = "";
                resultado = resource.query();	
                return resultado;
            },
            post: function (servicio,data) {
                console.log(data);
                var urlApi = "http://systab.herokuapp.com/";
                var resource   = $resource(urlApi + servicio),
                    resultado = "";
                resultado = resource.query();   
                return resultado;
            }

        }
    }]);        	