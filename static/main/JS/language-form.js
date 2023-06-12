'use strict';
document.addEventListener('DOMContentLoaded', function () {

  var formElement = document.getElementById('language-form');
  var selectElement = document.getElementById('language-select');

  selectElement.addEventListener('change', function () {
    formElement.submit();
  });

});

