angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            post: function (datos, servicio) {
                $http.defaults.headers.post['Content-Type'] = 'application/json; charset=UTF-8';
                var urlApi = "http://systab.herokuapp.com/";
                	resource   = $resource(urlApi + servicio),
                	resultado  = resource.save({}, datos);	
                return resultado;
            }
        }
    }]);        	