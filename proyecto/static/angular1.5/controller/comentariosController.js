angular.module('comentariosModuleController', [])

	.controller('comentariosController',['$scope', '$rootScope','ServiceHTTP','NgToast',
        function($scope,$rootScope,ServiceHTTP,NgToast)
        {
			$scope.queryObjModel = function () {
	    	    ServiceHTTP.query('service-comentarios-query/').$promise.then(function(result) {

				   $scope.postQuery = result;
				}, function(errResponse) {
				   console.log("error "+errResponse);
				});
    		}
			$scope.queryObjModel();

			$scope.SaveEditObjModel = function (id)
            {
            	$scope.ObjModel = {
            		pk:id
            	}
                ServiceHTTP.update('service-comentarios-query/',$scope.ObjModel).$promise.then(function(result) {
                	if(result.setCod == 0){
                		$scope.queryObjModel();
                		NgToast.msjToast({mensaje: 'Se activo el comentario correctamente.', clase: 'success'});
                	}else{
                		NgToast.msjToast({mensaje: 'Error al guardar.', clase: 'danger'});
                	}
                    
                }, function(errResponse) {
                   console.log("error "+JSON.stringify(errResponse));
                });
            }
        }
    ]);        	