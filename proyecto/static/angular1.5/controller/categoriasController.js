angular.module('categoriaModuleController', [])

	.controller('categoriaController',['$scope', '$rootScope','ServiceHTTP','$http',' $q',
        function($scope,$rootScope,ServiceHTTP,$http,)
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

            PostServiceTarifas.CancularTarifas($scope.formData).then(function (data) {
              //console.log(data);
              $scope.FormDataTarifa = data;//cargamos el json a el formulario
              //$scope.formData.cantidad = "";
            }, failureCb);

			$scope.saveCategorias = function ()
        	{
                ServiceHTTP.post('service-categorias-query/',$scope.categorias).then(function(result) {
                   $scope.postQuery = result;
                }, function(errResponse) {
                   console.log("error "+errResponse);
                });

        	}



        }
    ]);        	