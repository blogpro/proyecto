angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            post: function (datos, servicio) {
            	var urlApi = "http://systab.herokuapp.com/";

                //var resource = $resource("http://systab.herokuapp.com/service-post-query/");
                var resource   = $resource(urlApi + servicio);
				resource.query().$promise.then(function(todos) {
					   // success
					   console.log("success "+JSON.stringify(todos));
					}, function(errResponse) {
					   // fail
					   console.log("fail "+errResponse);
					});

                
                return 0;
            }
        }
    }]);        	