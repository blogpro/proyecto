angular.module('factoryModule', [])

	.factory('ServiceHTTP',function ($resource,$timeout) {
        var urlApi = "http://systab.herokuapp.com/",
            resource = "",
            resultado = "";
        return {
            query: function (url) {
                resource   = $resource(urlApi + url);
                resultado = resource.query();
                return resultado;
            },
            get: function (url,id) {
                resource   = $resource(urlApi + url+':id');
                resultado = resource.get({id:id});
                return resultado;
            },
            post: function (url,data) {
                resource   = $resource(urlApi + url);
                resultado = resource.save(data);   
                return resultado;
            },
            update: function (url,data) {
                return $resource(urlApi + url, null,{'update': { method:'PUT' }});
            }
        }
    })