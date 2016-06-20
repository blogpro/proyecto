angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$http',function ($resource, $rootScope, $http) {
        return {
            post: function (datos, servicio) {
                var urlApi = "http://systab.herokuapp.com/";
                	resource   = $resource(urlApi + "service-post-query/"),

                console.log("dato1 "+JSON.stringify(resource));
                return resultado;
            }
        }
    }]);        	