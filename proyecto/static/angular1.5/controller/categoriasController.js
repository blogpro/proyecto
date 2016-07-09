angular.module('categoriaModuleController', [])

	.controller('categoriaController',
        function($scope,$rootScope,ServiceHTTP,ServiceHTTP2)
        {
        	$scope.categorias = "";

        	$scope.queryCategorias = function () {
	    	    ServiceHTTP.query('service-categorias-query/').$promise.then(function(result) {
				   $scope.postQuery = result;
				}, function(errResponse) {
				   console.log("error "+errResponse);
				});
    		}
			$scope.queryCategorias();

			$scope.saveCategorias = function ()
        	{
                ServiceHTTP2.post('service-categorias-query/',$scope.categorias).then(function(result) {
                   console.log(result);
                }, function(errResponse) {
                   console.log("error "+errResponse);
                });
        	}

        }
    );        	