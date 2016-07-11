angular.module('factoryModule', [])

	.factory('ServiceHTTP', ['$resource', '$rootScope','$q','$http',function ($resource, $rootScope, $q, $http) {
        return {
            query: function (url) {
                var urlApi = "http://systab.herokuapp.com/";
                var resultado = "";

                var resource   = $resource(urlApi + url),
                resultado = resource.query();	
                return resultado;
            },
            post: function (url,data) {

                var url = 'http://systab.herokuapp.com/'+url;

                // var defer = $q.defer();
                // $http.post('http://systab.herokuapp.com/'+servicio, data).
                // success(function (data, status, headers, config) {
                //     defer.resolve(data);
                // }).error(function (data, status, headers, config) {
                //     defer.reject(status);
                // });
                // return defer.promise;
                console.log(data);
                var defer = $q.defer();
                $http({method: 'POST',
                    url: url,
                    data: data}).
                    success(function (data, status, headers, config) {
                        defer.resolve(data);
                    }).error(function (data, status, headers, config) {
                        defer.reject(status);
                    });
                return defer.promise;


            }

        }
    }])

.factory('ServiceHTTP2', ['$resource',function ($resource) {
        return $resource('http://systab.herokuapp.com/service-categorias-query/');
}])   



