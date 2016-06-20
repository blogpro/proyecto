angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            post: function (datos, servicio) {
                var urlApi = "http://systab.herokuapp.com/";
                	//resource   = $resource(urlApi + "service-post-query/"),
				urlApi.query().$promise.then(function(todos) {
					   // success
					   console.log("success "+JSON.stringify(todos));
					}, function(errResponse) {
					   // fail
					   console.log("fail "+errResponse);
					});

                
                return resultado;
            }
        }
    }]);        	