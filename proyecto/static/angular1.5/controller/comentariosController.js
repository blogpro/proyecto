angular.module('comentariosModuleController', [])

	.controller('comentariosController',['$scope', '$rootScope','ServiceHTTP',
        function($scope,$rootScope,ServiceHTTP)
        {
    	    ServiceHTTP.query('service-comentarios-query/').$promise.then(function(result) {
			   $scope.postQuery = result;
			}, function(errResponse) {
			   console.log("error "+errResponse);
			});
        }
    ]);        	