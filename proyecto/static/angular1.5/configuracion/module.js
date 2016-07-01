var angularRoutingApp = angular.module('blog', [
	'ngRoute',
    'ngResource',
    'factoryModule',
	'indexModuleController',
    'categoriaModuleController'
	]);

angularRoutingApp.config(function($interpolateProvider) {//codigo para cambiar la forma de mostrar en el template a // en lugar de {{}}
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

// Configuración de las rutas
angularRoutingApp.config(function($routeProvider) {

    $routeProvider
        .when('/', {
            templateUrl : '/index-list-post-angular/',
            controller  : 'indexController'
        })
        .when('/category-post', {
            templateUrl : '/category-post/',
            controller  : 'indexController'
        })
        .otherwise({
            redirectTo: '/'
        });
});