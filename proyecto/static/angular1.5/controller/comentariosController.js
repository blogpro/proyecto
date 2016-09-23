angular.module('comentariosModuleController', [])

	.controller('comentariosController',['$scope', '$rootScope','ServiceHTTP',
        function($scope,$rootScope,ServiceHTTP)
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
                    $scope.queryObjModel();
                }, function(errResponse) {
                   console.log("error "+JSON.stringify(errResponse));
                });
            }
        }
    ]);        	