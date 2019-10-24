'use strict';

angular.module('notemgr').
config(
    function (
        $locationProvider,
        $resourceProvider,
        $routeProvider
    ) {
        $locationProvider.html5Mode(true).hashPrefix('!');

        $resourceProvider.defaults.stripTrailingSlashes = false;
        $routeProvider.
        when("/", {
            template: "<note-list></note-list>"
        }).
        when("/note/add", {
            template: "<note-detail></note-detail>"
        }).
        when("/note/edit/:uuid", {
            template: "<note-detail></note-detail>"
        }).
        when("/login", {
            template: "<login-detail></login-detail>"
        }).
        when("/logout", {
            redirectTo: '/login'
        }).
        when("/register", {
            template: "<register-detail></register-detail>",
        }).
        otherwise({
            redirectTo: '/'
        });
    });