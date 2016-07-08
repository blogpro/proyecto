angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        return {
            query: function (servicio) {
            	var urlApi = "http://systab.herokuapp.com/";
                var resource   = $resource(urlApi + servicio),
                	resultado = "";
                resultado = resource.query();	
                return resultado;
            },
            post: function (servicio,data) {
                console.log(data);


                

                var urlApi = "http://systab.herokuapp.com/";
                var resource   = $resource(urlApi + servicio),

                resource.save({firstname:$scope.firstname,lastname:$scope.lastname,address:$scope.address,email:$scope.email}, function(response){
                        console.log(response.message);
                });


                var resultado = "";
                resultado = resource.save(data);
                console.log(resultado);
                return defer.promise;

                // var defer = $q.defer();
                // $http.post('http://systab.herokuapp.com/'+servicio, data).
                // success(function (data, status, headers, config) {
                //     defer.resolve(data);
                // }).error(function (data, status, headers, config) {
                //     defer.reject(status);
                // });
                // return defer.promise;

                
            }

        }
    }]);        	