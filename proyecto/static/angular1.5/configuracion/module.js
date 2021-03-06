var angularRoutingApp = angular.module('blog', [
  'ngRoute',
  'ngDialog',
  'ngResource',
  'ngToast',
  'sExternoModuleController',
  'factoryModule',
	'indexModuleController',
  'categoriaModuleController',
  'etiquetaModuleController',
  'comentariosModuleController',
  'statusModuleController'
	]);

angularRoutingApp.config(function($interpolateProvider) {//codigo para cambiar la forma de mostrar en el template a // en lugar de {{}}
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

angularRoutingApp.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';    }
);

angularRoutingApp.config(function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
  $resourceProvider.defaults.actions.update = {
      method: 'PUT'
    };
});

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
        .when('/tags-post/', {
            templateUrl : '/list-tag-angular/',//Url Servidor donde se hace la invocacion a el template que se cargara
            controller  : 'etiquetaController'
        })
        .when('/list-comentarios/', {
            templateUrl : '/list-comentarios-angular/',//Url Servidor donde se hace la invocacion a el template que se cargara
            controller  : 'comentariosController'
        })
        .when('/status-post/', {
            templateUrl : '/list-status-angular/',//Url Servidor donde se hace la invocacion a el template que se cargara
            controller  : 'statusController'
        })
        .otherwise({
            redirectTo: '/'
        });
});