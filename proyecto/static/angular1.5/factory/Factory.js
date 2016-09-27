angular.module('factoryModule', [])

	.factory('NgToast',function (ngToast,$timeout) {
        return {
            msjToast: function (opciones) {
                var options = {
                    content: opciones.mensaje,
                    animation: 'slide',
                    horizontalPosition: 'right',
                    verticalPosition: 'top',
                    maxNumber: 0,
                    className: opciones.clase,
                    timeout: 5000
                };
                $timeout(function () {
                    ngToast.create(options);
                }, 400);
            },
            confirm: function (){     
             ngDialog.openConfirm({
                    template:
                        '<p>Are you sure you want to delete selected conversation(s) ?</p>' +
                        '<div>' +
                          '<button type="button" class="btn btn-default" ng-click="closeThisDialog(0)">No&nbsp;' +
                          '<button type="button" class="btn btn-primary" ng-click="confirm(1)">Yes' +
                        '</button></div>',
                    plain: true,
                    className: 'ngdialog-theme-default'
                }).then(function (value) {
                    // perform delete operation
                }, function (value) {
                    //Do something 
                });
            }
        }
    })

    .factory('ServiceHTTP',function ($resource,$location) {
        var protocol = $location.protocol();
        var host = location.host;
        var urlApi = protocol+'://'+host+'/';
        //var urlApi = "http://systab.herokuapp.com/",
            resource = "",
            resultado = "";
        return {
            query: function (url) {
                resource   = $resource(urlApi + url);
                resultado = resource.query();
                return resultado;
            },
            get: function (url,id) {
                resource   = $resource(urlApi + url+':id');
                resultado = resource.get({id:id});
                return resultado;
            },
            post: function (url,data) {
                resource   = $resource(urlApi + url);
                resultado = resource.save(data);   
                return resultado;
            },
            borrar: function (url,id) {
                resource   = $resource(urlApi + url+':id');
                resultado = resource.delete({id:id});   
                return resultado;
            },
            update: function (url,data) {
                resource   = $resource(urlApi + url);
                resultado = resource.update(data);   
                return resultado;
            }
        }
    })
    
    .factory('ServiceHTTPExternos',function ($resource,$location) {
        var resource = "",
            resultado = "";
        return {
            query: function (url,servicio) {
                resource   = $resource(url + servicio);
                resultado = resource.query();
                return resultado;
            }
        }
    })