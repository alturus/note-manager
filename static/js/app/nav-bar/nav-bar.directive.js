'use strict';

angular.module("navBar").
    directive('navBar', function (Note, $cookies, $window, $location) {
        return {
            restrict: "E",
            templateUrl: "/templates/nav-bar.html",
            link: function (scope, element, attr) {
                scope.items = Note.query();
                scope.userLoggedIn = false;
                scope.$watch(function () {
                    var token = $window.localStorage.getItem('access_token');
                    if (token) {
                        scope.userLoggedIn = true;
                        scope.username = $cookies.get("username");
                    } else {
                        scope.userLoggedIn = false;
                    }
                });
            }
        };
    });