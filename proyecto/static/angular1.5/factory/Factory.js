angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            post: function (datos, servicio) {
                $http.defaults.headers.post['Content-Type'] = 'application/json; charset=UTF-8';
                var urlApi = "http://systab.herokuapp.com/";
                	resource   = $resource(urlApi + servicio),
                	resultado  = resource.save({}, datos);	
                console.log("dato1 "+JSON.stringify(resultado));
                resultado.$promise.then(function (result) {
	        		console.log("dato2 "+JSON.stringify(result));
	        	})
                return resultado;
            }
        }
    }]);        	