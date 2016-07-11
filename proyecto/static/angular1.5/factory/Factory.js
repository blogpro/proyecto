angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        var urlApi = "http://systab.herokuapp.com/";
        var resultado = "";
        return {
            query: function (url) {
                var resource   = $resource(urlApi + url),
                resultado = resource.query();	
                return resultado;
            },
            post: function (url,data) {
                var resource   = $resource(urlApi + url),
                resultado = resource.save(data);   
                return resultado;
            }
        }
    }])


