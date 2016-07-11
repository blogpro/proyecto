angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        return {
            query: function (url) {
                var urlApi = "http://systab.herokuapp.com/";
                var resultado = "";

                var resource   = $resource(urlApi + url),
                resultado = resource.query();	
                return resultado;
            },
            post: function (url,data) {

                var urlApi = "http://systab.herokuapp.com/";
                var resultado = "";

                var resource   = $resource(urlApi + url),
                resultado = resource.save(data);   
                return resultado;
            }
        }
    }]) 



