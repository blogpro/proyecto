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
                ServiceHTTP2.save($scope.categorias)
                
                var query = ServiceHTTP2.query();
                query.$promise.then(function(data) {
                     console.log(data);
                });
        	}

        }
    );        	