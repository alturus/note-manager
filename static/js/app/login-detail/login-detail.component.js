'use strict';

angular.module('loginDetail').
    component('loginDetail', {
        templateUrl: '/templates/login-detail.html',
        controller: function (
            $cookies,
            $window,
            $http,
            $location,
            $routeParams,
            $rootScope,
            $scope
        ) {
            var loginUrl = '/api/v1/users/token/';
            $scope.loginError = {};
            $scope.user = {
                username: $cookies.get("username")
            };

            $scope.$watch(function () {
                if ($scope.user.password) {
                    $scope.loginError.password = "";
                } else if ($scope.user.username) {
                    $scope.loginError.username = "";
                }
            });

            var tokenExists = $window.localStorage.getItem('access_token');
            if (tokenExists) {
                $scope.loggedIn = true;
                $window.localStorage.removeItem('access_token');
                window.location.reload()
            }

            $scope.doLogin = function (user) {
                if (!user.username) {
                    $scope.loginError.username = ["This field may not be blank."];
                }

                if (!user.password) {
                    $scope.loginError.password = ["This field is required."];
                }

                if (user.username && user.password) {
                    var reqConfig = {
                        method: "POST",
                        url: loginUrl,
                        data: {
                            username: user.username,
                            password: user.password
                        },
                        headers: {}
                    };

                    $http(reqConfig).then(function successCallback(response) {
                        $window.localStorage.setItem('access_token', response.data.access);
                        $http.defaults.headers.common.Authorization = 'Bearer ' + response.data.access;
                        $cookies.put("username", user.username);
                        var next_path = $location.search().next;
                        if (next_path) {
                            $location.path(next_path);
                        } else {
                            $location.path("/");
                        }
                    }, function errorCallback(response) {
                        $scope.loginError = response.data;
                    });
                }
            };
        }
    });