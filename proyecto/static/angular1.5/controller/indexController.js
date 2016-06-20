angular.module('indexModuleController', [])

	.controller('indexController',['$scope', '$rootScope','ServiceHTTP',
        function($scope,$rootScope,ServiceHTTP)
        {
        	ServiceHTTP.post('','service-post-query/').$promise.then(function (result) {
        		console.log(result);
        	})

        }
    ]);        	