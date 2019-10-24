'use strict';

angular.module('noteDetail').
    component('noteDetail', {
        templateUrl: '/templates/note-detail.html',
        controller: function (Category, Note, $cookies, $http, $location, $routeParams, $scope) {
            $scope.loading = true;
            $scope.note = null;
            $scope.pageError = false;
            $scope.notFound = false;
            $scope.categories = [];

            Category.query({}, function (data) {
                var categoryCount = data.length;
                for (var i = 0; i < categoryCount; i++) {
                    $scope.categories.push(data[i].name);
                }
                if (!$scope.note) {
                    $scope.noteCategory = $scope.categories[0];
                }
            });

            function postDataSuccess(data) {
                $scope.loading = false;
                $scope.note = data;
                var index = $scope.categories.indexOf(data.category);
                $scope.noteCategory = $scope.categories[index];
            }

            function postDataError(e_data) {
                $scope.loading = false;
                if (e_data.status == 404) {
                    $scope.notFound = true;
                } else {
                    $scope.pageError = true;
                }
            }

            var uuid = $routeParams.uuid;
            if (uuid) {
                Note.get({
                    "uuid": uuid
                }, postDataSuccess, postDataError);
            }

            $scope.deleteComment = function (comment) {
                comment.$delete({
                    "id": comment.id
                }, function (data) {
                    var index = $scope.comments.indexOf(comment);
                    $scope.comments.splice(index, 1);
                }, function (e_data) {
                    console.log(e_data);
                });
            };

            $scope.saveNote = function () {
                if ($scope.note && $scope.note.uuid) {
                    Note.update({
                        "uuid": $scope.note.uuid,
                        body: $scope.note.body,
                        title: $scope.note.title,
                        category: $scope.noteCategory,
                        is_favorited: $scope.note.is_favorited,
                        is_published: $scope.note.is_published
                    }, function (data) {
                        $location.path("/");
                    }, function (e_data) {
                        $scope.noteError = e_data.data;
                    });
                } else {
                    Note.create({
                        body: $scope.note.body,
                        title: $scope.note.title,
                        category: $scope.noteCategory,
                        is_favorited: $scope.note.is_favorited,
                        is_published: $scope.note.is_published
                    }, function (data) {
                        $location.path("/");
                    }, function (e_data) {
                        $scope.noteError = e_data.data;
                    });
                }
            };

            if ($scope.notFound) {
                $location.path("/");
            }
        }
    });