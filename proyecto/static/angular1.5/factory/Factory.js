angular.module('factoryModule', [])

	.factory('ServiceHTTP',function ($resource,$timeout) {
        var urlApi = "http://systab.herokuapp.com/",
            resource = "",
            resultado = "";

            $timeout(function () {

                return {
            query: function (url) {
                resource   = $resource(urlApi + url);
                resultado = resource.query();

                resultado.$promise.then(function(result) {
                    
                    
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

            }, 1200);

        
    })


