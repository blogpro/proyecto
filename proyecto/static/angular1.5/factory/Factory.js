angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http','$q',function ($resource, $rootScope, $http, $q) {
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
                var defer = $q.defer();

                $http.post('/api_add_licencia/', data, {transformRequest: angular.identity,headers: {'Content-Type': undefined}
                }).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                }).error(function (data, status, headers, config) {
                    defer.reject(status);
                });
                return defer.promise;

                
            }

        }
    }]);        	