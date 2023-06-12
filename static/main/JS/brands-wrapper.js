'use strict';
document.addEventListener('DOMContentLoaded', function () {

    var formElement = document.getElementById('language-form');
    var selectElement = document.getElementById('language-select');

    selectElement.addEventListener('change', function () {
        formElement.submit();
    });

    const brandsWrapper = document.querySelector('.brands-wrapper');
    const scrollLeftButton = document.querySelector('.scroll-left');
    const scrollRightButton = document.querySelector('.scroll-right');

    scrollLeftButton.addEventListener('click', function () {
        brandsWrapper.scrollBy({
            left: -100,
            behavior: 'smooth'
        });
    });

    scrollRightButton.addEventListener('click', function () {
        brandsWrapper.scrollBy({
            left: 100,
            behavior: 'smooth'
        });
    });

});