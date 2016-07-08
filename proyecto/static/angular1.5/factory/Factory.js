angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        return {
            query: function (servicio) {
            	var urlApi = "http://systab.herokuapp.com/";
                var resource   = $resource(urlApi + servicio),
                	resultado = "";
                resultado = resource.query();	
                return resultado;
            },
            post: function (servicio,data) {
                $http.defaults.headers.post['Content-Type'] = 'application/json; charset=UTF-8';
                var urlApi = "http://systab.herokuapp.com/";
                var resource   = $resource(urlApi + servicio);



                var resultado = resource.save(data);

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