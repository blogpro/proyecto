angular.module('etiquetaModuleController', [])

	.controller('etiquetaController',
        function($scope,$timeout,ServiceHTTP,ngDialog,NgToast)
        {
        	$scope.ObjModel = "";
            $scope.banderasbtn = {
                showBtnSave: true,
                showBtnEdit: false
            };

        	$scope.queryObjModel = function () {
	    	    ServiceHTTP.query('service-etiquetas-query/').$promise.then(function(result) {

				   $scope.postQuery = result;
				}, function(errResponse) {
				   console.log("error "+errResponse);
				});
    		}
			$scope.queryObjModel();

			$scope.saveObjModel = function ()
        	{
                ServiceHTTP.post('service-etiquetas-query/',$scope.categorias).$promise.then(function(result) {
                    if(result.setCod == 0){
                        $scope.ObjModel = "";
                        $scope.queryObjModel();
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
                $scope.banderasbtn.showBtnEdit = true;
                $scope.banderasbtn.showBtnSave = false;

                ServiceHTTP.get('service-categorias-query/',id).$promise.then(function(result) {
                    $scope.ObjModel = result;
                }, function(errResponse) {
                   console.log("error "+JSON.stringify(errResponse));
                });
            }
            $scope.SaveEditCat = function ()
            {
                ServiceHTTP.update('service-categorias-query/',$scope.categorias).$promise.then(function(result) {
                    $scope.ObjModel = "";
                    $scope.queryObjModel();
                }, function(errResponse) {
                   console.log("error "+JSON.stringify(errResponse));
                });
            }
            $scope.DeleteCategoria = function (id)
            {
                ServiceHTTP.borrar('service-categorias-query/',id).$promise.then(function(result) {
                    $scope.queryObjModel();
                }, function(errResponse) {
                   console.log("error "+JSON.stringify(errResponse));
                });
            }
            $scope.cancelCategorias = function ()
            {
                $scope.banderasbtn.showBtnSave = true;
                $scope.banderasbtn.showBtnEdit = false;
            }

        }
    );        	