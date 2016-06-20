angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            query: function (servicio) {

            	var urlApi = "http://systab.herokuapp.com/";
                var resource   = $resource(urlApi + servicio),
                	resultado = "";

				resource.query().$promise.then(function(result) {
					   resultado = result;
					}, function(errResponse) {
					   resultado = errResponse;
					});
                
                console.log("re "+resultado);

                return resultado;
            }
        }
    }]);        	