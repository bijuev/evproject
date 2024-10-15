(function ($) {

    AOS.init();

    // ========================
    // mobile menu
    // ========================
    $('.js-mob-tog').click(function (e) {
        e.preventDefault();
        $('body').toggleClass('overflow-hidden');
        $('.js-mob-tog, .bk-mob-nav, .bk-wrapper, .bk-header, .bk-notice').toggleClass(
            'active');
    });
    $('.js-mob-list').on('click', 'button', function (e) {
        e.preventDefault();
        $(this).parent().toggleClass('active');
        $(this).next().next().slideToggle();
    });

    $(document).ready(function () {
        $('.js-notice-bk').parent().height($('.js-notice-bk').outerHeight());
        $('.js-mob-list .menu-item-has-children').prepend('<button type="button"><span class="sr-only">Open Sub Menu</span></button>');
    });

    // ========================
    // fixed header
    // ========================

    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        if (scroll > 50) {
            $(".bk-header").addClass("fixed-top");
        } else {
            $(".bk-header").removeClass("fixed-top");
        }
    });

    $('#navs li a').on('click', function (event) {
        event.preventDefault();
        var targetID = $(this).attr('href');
        if(targetID === '#home'){
            $('html, body').animate({
                scrollTop: 0
            });
            return
        }
        var header_height = $('.bk-header').outerHeight();
        $('html, body').animate({
            scrollTop: $(targetID).offset().top - (header_height + 10)
        }); 
    });

    $('#mob-navs li a').on('click', function (event) {
        event.preventDefault();
        var targetID = $(this).attr('href');
        if(targetID === '#home'){
            $('html, body').animate({
                scrollTop: 0
            });
            return
        }
        var header_height = $('.bk-header').outerHeight();
        $('html, body').animate({
            scrollTop: $(targetID).offset().top - (header_height + 10)
        }); 
        $('body').removeClass('overflow-hidden');
        $('.js-mob-tog, .bk-mob-nav, .bk-wrapper, .bk-header, .bk-notice').removeClass(
            'active');
    });

    $('.go-to-down').on('click', function(){
        var header_height = $('.bk-header').outerHeight();
        $('html, body').animate({
            scrollTop: $('#find-near-plugs').offset().top - (header_height + 10)
        }); 
    });


})(jQuery);
