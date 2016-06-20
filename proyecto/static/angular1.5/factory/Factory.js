angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            post: function (datos, servicio) {
            	var urlApi = "http://systab.herokuapp.com/";
                var resource   = $resource(urlApi + servicio);

				resource.query().$promise.then(function(todos) {
					   console.log("success "+JSON.stringify(todos));
					}, function(errResponse) {
					   console.log("fail "+errResponse);
					});

                console.log("e "+resource.query());
                return 0;
            }
        }
    }]);        	