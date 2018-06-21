// $(document).ready(function () {
//     setTimeout(function () {
//         initTopSwiper()
//     },100)
//
// });
$(function(){

    initTopSwiper();

    initMenuSwiper();

});


function initTopSwiper(){

    var swiper = new Swiper("#topSwiper", {

        loop: true,
        autoplay:2000,
        pagination:".swiper-pagination",

    })
}


function initMenuSwiper(){

    var swiper = new Swiper("#swiperMenu", {
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 2,
        loop:true,
    })
}