angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            query: function (datos, servicio) {
            	var urlApi = "http://systab.herokuapp.com/";
                var resource   = $resource(urlApi + servicio);

                console.log("e "+resource.query());
                
				resource.query().$promise.then(function(todos) {
					   console.log("success "+JSON.stringify(todos));
					}, function(errResponse) {
					   console.log("fail "+errResponse);
					});

                
                return 0;
            }
        }
    }]);        	