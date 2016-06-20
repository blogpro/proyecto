angular.module('indexModuleController', [])

	.controller('indexController',['$scope', '$rootScope','ServiceHTTP',
        function($scope,$rootScope,ServiceHTTP)
        {
        	$scope.postQuery = ServiceHTTP.query('service-post-query/');

        }
    ]);        	