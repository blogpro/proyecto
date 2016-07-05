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
                var url = "http://systab.herokuapp.com/"+servicio;
                var defer = $q.defer();
                    $http({method: 'POST',
                    url: url,
                    data: data}).
                    success(function (data, status, headers, config) {
                        defer.resolve(data);
                    }).error(function (data, status, headers, config) {
                        defer.reject(status);
                    });
            return defer.promise;
            }

        }
    }]);        	