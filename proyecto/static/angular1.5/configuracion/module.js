var angularRoutingApp = angular.module('blog', ['ngRoute']);

// Configuración de las rutas
angularRoutingApp.config(function($routeProvider) {

    $routeProvider
        .when('/prueba-angular', {
            templateUrl : 'pages/acerca.html',
            //controller  : 'aboutController'
        })
        .otherwise({
            redirectTo: '/'
        });
});