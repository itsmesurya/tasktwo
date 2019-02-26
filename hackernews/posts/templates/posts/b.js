//
// angular.module('app', ['ngMaterial'])
//   .controller('Ctrl', function($scope, $http) {
//                $http.get('https://jsonplaceholder.typicode.com/users')
//       .then(function(response) {
//         $scope.persons = response.data;
//                });
// var i = function($scope) {
//     $scope.init = function(count) {
//         $scope.count = count;
//     }
// };
//   });

$(function() {

  var count = $('#count').val();


  $('#upvote').on('click', function(){
    count++;
    $('#count').html(count);
  });

  $('#downvote').on('click', function(){
    count--;
    $('#count').html(count);
  });

});
