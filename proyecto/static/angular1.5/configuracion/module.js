var angularRoutingApp = angular.module('blog', [
	'ngRoute',
	'indexModule'
	]);

// Configuración de las rutas
angularRoutingApp.config(function($routeProvider) {

    $routeProvider
        .when('/acerca', {
            templateUrl : 'inicio/templates/acercaAngular.html',
            controller  : 'indexController'
        })
        .otherwise({
            redirectTo: '/'
        });
});