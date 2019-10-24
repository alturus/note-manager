'use strict';

angular.module('noteList').
    component('noteList', {
        templateUrl: '/templates/note-list.html',
        controller: function (Note, $cookies, $location, $routeParams, $rootScope, $uibModal, $scope) {

            $scope.itemsPerPage = 5;
            $scope.currentPage = 1;

            $scope.sortType = '-created';

            // string manipulation functions
            function matchFirstChar(c, string) {
                return (string.charAt(0) == c);
            }

            function removeFirstChar(string) {
                return string.slice(1);
            }

            function removeDash(label) {
                if (matchFirstChar('-', label)) {
                    return removeFirstChar(label);
                }
                return label;
            }
            function addDash(label) {
                if (!matchFirstChar('-', label)) {
                    return '-' + label;
                }
                return label;
            }

            // sort functions
	        // add or remove '-' to sort up or down
            $scope.sortReverse = function(set) {
                set = set || false;
                if (set || !matchFirstChar('-', $scope.sortType)) {
                    $scope.sortType = addDash($scope.sortType);
                } else {
                    $scope.sortType = removeDash($scope.sortType);
                }
            };

            // sort a column with a single data attribute
            $scope.singleSort = function(label) {
                if ($scope.sortType == label) {
                    $scope.sortReverse();
                } else {
                    $scope.sortType = label;
                }
                $scope.pageChanged()
            };

            // boolean functions for detecting how a column is sorted
            // used for the up and down carets next to each column header
            $scope.sortAscend = function(label1, label2) {
                label2 = label2 || '';
                return ($scope.sortType == label1 || $scope.sortType == label2);
            };

            $scope.sortDescend = function(label1, label2) {
                label2 = label2 || '';
                return ($scope.sortType == ('-' + label1) || $scope.sortType == ('-' + label2));
            };

            $scope.favNote = function (note, val) {
                Note.update({
                    "uuid": note.uuid,
                    is_favorited: val
                }, function (data) {
                    var index = $scope.items.indexOf(note);
                    $scope.items[index] = data;
                }, function (e_data) {
                    console.log(e_data);
                });
            };

            $scope.pubNote = function (note, val) {
                Note.update({
                    "uuid": note.uuid,
                    is_published: val
                }, function (data) {
                    var index = $scope.items.indexOf(note);
                    $scope.items[index] = data;
                }, function (e_data) {
                    console.log(e_data);
                });
            };

            $scope.pageChanged = function () {
                Note.query({
                    "offset": ($scope.currentPage - 1) * $scope.itemsPerPage,
                    "limit": $scope.itemsPerPage,
                    "ordering": $scope.sortType
                }, function (data) {
                    $scope.items = data.results;
                    $scope.totalItems = data.count;
                }, function (errorData) {

                });
            };

            $scope.deleteNote = function (note) {
                Note.delete({
                    "uuid": note.uuid
                }, function (data) {
                    var index = $scope.items.indexOf(note);
                    $scope.items.splice(index, 1);
                    $scope.totalItems -= 1;
                    $scope.pageChanged();
                }, function (e_data) {
                    console.log(e_data);
                });
            };

            $scope.askDeleteNote = function (item) {
                var message = "Удалить '" + item.title + "' ?";

                var modalHtml = '<div class="modal-body">' + message + '</div>';
                modalHtml += '<div class="modal-footer"><button class="btn btn-danger" ng-click="ok()">УДАЛИТЬ</button><button class="btn btn-secondary" ng-click="cancel()">Отменить</button></div>';

                var modalInstance = $uibModal.open({
                    template: modalHtml,
                    controller: function ($scope) {
                        $scope.ok = function () {
                            modalInstance.close();
                        };
                        $scope.cancel = function () {
                            modalInstance.dismiss('cancel');
                        };
                    }
                });
                modalInstance.result.then(function () {
                    $scope.deleteNote(item);
                });
            };

            $scope.pageChanged()

        }
    });