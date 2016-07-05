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

angularRoutingApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';    }
]);

// Configuración de las rutas
angularRoutingApp.config(function($routeProvider) {

    $routeProvider
        .when('/', {
            templateUrl : '/index-dash-post-angular/',//Url Servidor donde se hace la invocacion a el template que se cargara
            controller  : 'indexController'
        })
        .when('/list-post/', {
            templateUrl : '/list-post-angular/',//Url Servidor donde se hace la invocacion a el template que se cargara
            controller  : 'indexController'
        })
        .when('/category-post/', {
            templateUrl : '/list-cat-angular/',//Url Servidor donde se hace la invocacion a el template que se cargara
            controller  : 'categoriaController'
        })
        .otherwise({
            redirectTo: '/'
        });
});