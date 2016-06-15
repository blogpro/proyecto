var angularRoutingApp = angular.module('blog', [
	'ngRoute',
	'indexModule'
	]);

// Configuración de las rutas
angularRoutingApp.config(function($routeProvider) {

    $routeProvider
        .when('/', {
            templateUrl : '/index-list-post-anglar/',
            controller  : 'indexController'
        })
        .when('/acerca', {
            templateUrl : '/acerca/',
            controller  : 'indexController'
        })
        .otherwise({
            redirectTo: '/'
        });
});