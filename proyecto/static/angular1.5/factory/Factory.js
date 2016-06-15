angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            post: function (datos, servicio) {
                $http.defaults.headers.post['Content-Type'] = 'application/json; charset=UTF-8';
                var resultado = 0;
                return resultado;
            }
        }
    }]);        	