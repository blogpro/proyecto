var angularRoutingApp = angular.module('blog', [
	'ngRoute',
	'indexModule'
	]);

// Configuración de las rutas
angularRoutingApp.config(function($routeProvider) {

    $routeProvider
        .when('/prueba-angular', {
            templateUrl : 'static/index.html',
            //controller  : 'aboutController'
        })
        .otherwise({
            redirectTo: '/'
        });
});