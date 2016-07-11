angular.module('categoriaModuleController', [])

	.controller('categoriaController',
        function($scope,$timeout,ServiceHTTP)
        {
        	$scope.categorias = "";

            $scope.queryCategorias = function () {
                $timeout(function () {
                    $scope.postQuery = ServiceHTTP.query('service-categorias-query/');
                    console.log($scope.postQuery);
                }, 1200);
                
            }

    //     	$scope.queryCategorias = function () {
	   //  	    ServiceHTTP.query('service-categorias-query/').$promise.then(function(result) {
				//    $scope.postQuery = result;
				// }, function(errResponse) {
				//    console.log("error "+errResponse);
				// });
    // 		}
			$scope.queryCategorias();

			$scope.saveCategorias = function ()
        	{

                ServiceHTTP.post('service-categorias-query/',$scope.categorias).$promise.then(function(result) {
                   console.log(result)
                }, function(errResponse) {
                   console.log("error "+errResponse);
                });
        	}

        }
    );        	