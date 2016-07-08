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
                    resultado = "";
                resultado = resource.save(data);
                console.log(resultado);
                return resultado;

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

    .factory('ServiceHTTP2', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        return {
            var src = $resource('http://systab.herokuapp.com/service-categorias-query',
              //{id: "@id", cmd: "@cmd"}, //parameters default
              {
                ListTodos: { method: "GET", params: {} },
                GetTodo: { method: "GET", params: { id: 0 } },                            
                post: { method: "POST", params: { content: "", order: 0, done: false } },
                UpdateTodo: { method: "PATCH", params: { /*...*/ } },
                DeleteTodo: { method: "DELETE", params: { id: 0 } },
                ResetTodos: { method: "GET", params: { cmd: "reset" } },
              });
            return src;
        }
    }]);        	