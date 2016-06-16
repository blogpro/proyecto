var angularRoutingApp = angular.module('blog', [
	'ngRoute',
	'indexModuleController'
	]);

// Configuración de las rutas
angularRoutingApp.config(function($routeProvider) {

    $routeProvider
        .when('/', {
            templateUrl : '/index-list-post-angular/',
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