angular.module('categoriaModuleController', [])

	.controller('categoriaController',['$scope', '$rootScope','ServiceHTTP','ServiceHTTP2',
        function($scope,$rootScope,ServiceHTTP)
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
        		console.log($scope.categorias.title);
                ServiceHTTP2.post('service-categorias-query/',$scope.categorias).$promise.then(function(result) {
                   $scope.postQuery = result;
                }, function(errResponse) {
                   console.log("error "+errResponse);
                });
        	}



        }
    ]);        	