angular.module('sExternoModuleController', [])

	.controller('indexController',['$scope', '$rootScope','ServiceHTTPExternos',
        function($scope,$rootScope,ServiceHTTPExternos)
        {
    	    ServiceHTTPExternos.query('http://admin.creaturviajes.com/','ws/tipocambio/').$promise.then(function(result) {
			   $scope.postQuery = result;
			}, function(errResponse) {
			   console.log("error "+errResponse);
			});
        }
    ]);        	