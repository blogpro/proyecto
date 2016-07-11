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
                   var resultado2 =  result;
                }, function(errResponse) {
                   console.log("error "+errResponse);
                });
                return resultado2;
            },
            post: function (url,data) {
                resource   = $resource(urlApi + url);
                resultado = resource.save(data);   
                return resultado;
            }
        }
    }])


