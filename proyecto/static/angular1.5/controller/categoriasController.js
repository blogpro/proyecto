angular.module('categoriaModuleController', [])

	.controller('categoriaController',['$scope', '$rootScope','ServiceHTTP',
        function($scope,$rootScope,ServiceHTTP)
        {
    	    ServiceHTTP.query('service-post-query/').$promise.then(function(result) {
			   $scope.postQuery = result;
			}, function(errResponse) {
			   console.log("error "+errResponse);
			});
        }
    ]);        	