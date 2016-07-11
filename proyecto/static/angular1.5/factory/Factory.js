angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        var urlApi = "http://systab.herokuapp.com/";
        var resultado = "";
        
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

.factory('ServiceHTTP2', ['$resource',function ($resource) {
        return $resource('http://systab.herokuapp.com/service-categorias-query/');
}])   



