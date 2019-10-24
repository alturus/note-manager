'use strict';

angular.module('registerDetail').
    component('registerDetail', {
        templateUrl: '/templates/register-detail.html',
        controller: function (
            $cookies,
            $http,
            $location,
            $window,
            $routeParams,
            $rootScope,
            $scope
        ) {
            var registerUrl = '/api/v1/users/';
            $scope.registerError = {};
            $scope.user = {};

            $scope.$watch(function () {
                if ($scope.user.password1) {
                    $scope.registerError.password1 = "";
                } else if ($scope.user.password2) {
                    $scope.registerError.password2 = "";
                } else if ($scope.user.username) {
                    $scope.registerError.username = "";
                }
            });

            $scope.doRegister = function (user) {
                if (!user.username) {
                    $scope.registerError.username = ["Поле не должно быть пустым"];
                }

                if (!user.password1) {
                    $scope.registerError.password1 = ["Поле не может быть пустым"];
                }

                if (!user.password2) {
                    $scope.registerError.password2 = ["Поле не может быть пустым"];
                }

                if (user.password1 && user.password1 != user.password2) {
                    console.log('password 2 :' + user.password2);
                    $scope.registerError.password = ["Пароли не совпадают"];
                }

                if (user.username && user.password1 == user.password2) {
                    var reqConfig = {
                        method: "POST",
                        url: registerUrl,
                        data: {
                            username: user.username,
                            password: user.password2
                        },
                        headers: {}
                    };

                    $http(reqConfig).then(function successCallback(response) {
                        $window.localStorage.setItem('access_token', response.data.access);
                        $http.defaults.headers.common.Authorization = 'Bearer ' + response.data.access;
                        $cookies.put("username", response.data.username);
                        $location.path("/");
                    }, function errorCallback(response) {
                        $scope.registerError = response.data;
                    });
                }
            };
        }
    });