angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        return {

            var urlApi = "http://systab.herokuapp.com/";
            var resultado = "";

            query: function (servicio) {
                var resource   = $resource(urlApi + servicio),
                resultado = resource.query();	
                return resultado;
            },
            post: function (servicio,data) {

                var resource = $resource(urlApi + servicio, {}, {method:'POST'});
                resultado = resource.save(data);
                return resultado;

                // var defer = $q.defer();
                // $http.post('http://systab.herokuapp.com/'+servicio, data).
                // success(function (data, status, headers, config) {
                //     defer.resolve(data);
                // }).error(function (data, status, headers, config) {
                //     defer.reject(status);
                // });
                // return defer.promise;

                
            }

        }
    }]);        	