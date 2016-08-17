angular.module('etiquetaModuleController', [])

	.controller('etiquetaController',
        function($scope,$timeout,ServiceHTTP,ngDialog,NgToast)
        {
        	$scope.categorias = "";
            $scope.banderasCategorias = {
                showBtnSave: true,
                showBtnEdit: false
            };

        	$scope.queryCategorias = function () {
	    	    ServiceHTTP.query('service-etiquetas-query/').$promise.then(function(result) {

				   $scope.postQuery = result;
				}, function(errResponse) {
				   console.log("error "+errResponse);
				});
    		}
			$scope.queryCategorias();

			$scope.saveCategorias = function ()
        	{
                ServiceHTTP.post('service-categorias-query/',$scope.categorias).$promise.then(function(result) {
                    if(result.setCod == 0){
                        $scope.categorias = "";
                        $scope.queryCategorias();
                        NgToast.msjToast({mensaje: 'Guardado correctamente.', clase: 'success'});
                    }else{
                        NgToast.msjToast({mensaje: 'Error al guardar.', clase: 'danger'});
                    }
                }, function(errResponse) {
                   console.log("error "+JSON.stringify(errResponse));
                });
        	}

            $scope.EditarCategoria = function (id)
            {
                $scope.banderasCategorias.showBtnEdit = true;
                $scope.banderasCategorias.showBtnSave = false;

                ServiceHTTP.get('service-categorias-query/',id).$promise.then(function(result) {
                    $scope.categorias = result;
                }, function(errResponse) {
                   console.log("error "+JSON.stringify(errResponse));
                });
            }
            $scope.SaveEditCat = function ()
            {
                ServiceHTTP.update('service-categorias-query/',$scope.categorias).$promise.then(function(result) {
                    $scope.categorias = "";
                    $scope.queryCategorias();
                }, function(errResponse) {
                   console.log("error "+JSON.stringify(errResponse));
                });
            }
            $scope.DeleteCategoria = function (id)
            {
                ServiceHTTP.borrar('service-categorias-query/',id).$promise.then(function(result) {
                    $scope.queryCategorias();
                }, function(errResponse) {
                   console.log("error "+JSON.stringify(errResponse));
                });
            }
            $scope.cancelCategorias = function ()
            {
                $scope.banderasCategorias.showBtnSave = true;
                $scope.banderasCategorias.showBtnEdit = false;
            }

        }
    );        	