var angularRoutingApp = angular.module('blog', [
	'ngRoute',
	'indexModule'
	]);

// Configuración de las rutas
angularRoutingApp.config(function($routeProvider) {

    $routeProvider
        .when('/acerca', {
            templateUrl : 'static/acerca.html',
            //controller  : 'aboutController'
        })
        .otherwise({
            redirectTo: '/'
        });
});