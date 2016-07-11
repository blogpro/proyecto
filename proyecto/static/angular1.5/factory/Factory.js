angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        var urlApi = "http://systab.herokuapp.com/",
            resource = "",
            resultado = "";

        return {
            query: function (url) {
                resource   = $resource(urlApi + url);
                resultado = resource.query();
                
                resultado.$promise.then(function(result) {
                   return result;
                }, function(errResponse) {
                   console.log("error "+errResponse);
                });
            },
            post: function (url,data) {
                resource   = $resource(urlApi + url);
                resultado = resource.save(data);   
                return resultado;
            }
        }
    }])


