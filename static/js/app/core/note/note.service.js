'use strict';

angular.
    module('core.note').
        factory('Note', function (LoginRequiredInterceptor, $cookies, $window, $http, $httpParamSerializer, $location, $resource) {
            var url = '/api/v1/notes/:uuid/';

            var noteQuery = {
                method: "GET",
                params: {
                    "offset": "@offset",
                    "limit": "@limit",
                    "ordering": "@ordering"
                },
                isArray: false,
                cache: false,
                transformResponse: function (data, headersGetter, status) {
                    var finalData = angular.fromJson(data);
                    return finalData;
                },
                interceptor: {
                    responseError: LoginRequiredInterceptor
                }
            };

            var noteGet = {
                method: "GET",
                params: {
                    "uuid": "@uuid"
                },
                isArray: false,
                cache: false,
                interceptor: {
                    responseError: LoginRequiredInterceptor
                }
            };

            var noteCreate = {
                url: '/api/v1/notes/',
                method: "POST",
                interceptor: {
                    responseError: LoginRequiredInterceptor
                }
            };

            var noteUpdate = {
                method: "PATCH",
                params: {
                    "uuid": "@uuid"
                },
                isArray: false,
                cache: false,
                interceptor: {
                    responseError: LoginRequiredInterceptor
                }
            };

            var noteDelete = {
                method: "DELETE",
                params: {
                    "uuid": "@uuid"
                },
                isArray: false,
                cache: false,
                interceptor: {
                    responseError: LoginRequiredInterceptor
                }
            };

            var token = $window.localStorage.getItem('access_token');
            if (token) {
                $http.defaults.headers.common.Authorization = 'Bearer ' + token;
            }

            return $resource(url, {}, {
                query: noteQuery,
                get: noteGet,
                create: noteCreate,
                update: noteUpdate,
                delete: noteDelete
            });
        });