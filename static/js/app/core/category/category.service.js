'use strict';

angular.
    module('core.category').
        factory('Category', function ($http, $httpParamSerializer, $resource) {
            var url = '/api/v1/categories/';

            var categoryQuery = {
                method: "GET",
                params: {},
                isArray: true,
                cache: false,
                transformResponse: function (data, headersGetter, status) {
                    var finalData = angular.fromJson(data);
                    return finalData;
                },
            };

            return $resource(url, {}, {
                query: categoryQuery
            });

        });