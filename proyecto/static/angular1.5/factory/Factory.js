angular.module('factoryModule', [])

	.factory('ServiceHTTP',function ($resource,$timeout) {
        var urlApi = "http://systab.herokuapp.com/",
            resource = "",
            resultado = "";

        return {
            query: function (url) {
                resource   = $resource(urlApi + url);
                resultado = resource.query();

                resultado.$promise.then(function(result) {
                    $timeout(function () {
                        return result;
                    }, 1200);
                }, function(errResponse) {
                   console.log("error "+errResponse);
                });
                console.log("exit");
            },
            post: function (url,data) {
                resource   = $resource(urlApi + url);
                resultado = resource.save(data);   
                return resultado;
            }
        }
    })


