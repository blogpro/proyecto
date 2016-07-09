angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        return {
            query: function (servicio) {
                var urlApi = "http://systab.herokuapp.com/";
                var resultado = "";

                var resource   = $resource(urlApi + servicio),
                resultado = resource.query();	
                return resultado;
            },
            post: function (servicio,data) {

                var defer = $q.defer();
                $http.post('http://systab.herokuapp.com/'+servicio, data).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                }).error(function (data, status, headers, config) {
                    defer.reject(status);
                });
                return defer.promise;
            }

        }
    }])

.factory('ServiceHTTP2', ['$resource',function ($resource) {
        return $resource('http://systab.herokuapp.com/service-categorias-query/', 
            {id:'@id'},
            {method:'POST'}
        );
}])   



