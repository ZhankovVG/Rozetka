var indexValue = 0;
var timer;

function SlideShow() {
    timer = setTimeout(SlideShow, 3500)
    var x;
    const elements = document.querySelectorAll('.slider__img');
    for (x = 0; x < elements.length; x++) {
        elements[x].style.display = "none";
    }
    indexValue++;
    if (indexValue > elements.length) {
        indexValue = 1;
    }
    elements[indexValue - 1].style.display = "block";
}
SlideShow();

function prevSlide() {
    clearTimeout(timer);
    const elements = document.querySelectorAll('.slider__img');
    if (indexValue == 1) {
        indexValue = elements.length;
    } else {
        indexValue--;
    }
    for (let i = 0; i < elements.length; i++) {
        elements[i].style.display = "none";
    }
    elements[indexValue - 1].style.display = "block";
}

function nextSlide() {
    clearTimeout(timer);
    const elements = document.querySelectorAll('.slider__img');
    if (indexValue == elements.length) {
        indexValue = 1;
    } else {
        indexValue++;
    }
    for (let i = 0; i < elements.length; i++) {
        elements[i].style.display = "none";
    }
    elements[indexValue - 1].style.display = "block";
}

