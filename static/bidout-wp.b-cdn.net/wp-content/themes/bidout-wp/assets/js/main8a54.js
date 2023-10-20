(function ($) {
  "use strict";

  //Preloader
  jQuery(window).on('load', function () {
    $(".egns-preloader").delay(1600).fadeOut("slow");
  });

  jQuery('.dokan-dashboard-wrap').parents('body').addClass('dokan-dashboard');


  // sticky header with theme option enabel disable
  if (egns_theme_options.sticky_header_enable != 0) {
    window.addEventListener('scroll', function () {
      const header = document.querySelector('header.style-1, header.style-2, header.style-3');
      header.classList.toggle("sticky", window.scrollY > 0);
    });
  }

  // mobile-search-area
  $('.search-btn').on("click", function () {
    $('.mobile-search').addClass('slide');
  });

  $('.search-cross-btn').on("click", function () {
    $('.mobile-search').removeClass('slide');
  });

  // Sub Submenu Class
  $('#menu-main-menu .sub-menu').parents('li').addClass('menu-item-has-children');
  // mobile-menu
  $('.mobile-menu-btn').on("click", function () {
    $('.main-menu').addClass('show-menu');
  });

  $('.menu-close-btn').on("click", function () {
    $('.main-menu').removeClass('show-menu');
  });

  // mobile-drop-down
  $('i').on('click', function () {
    $(this).toggleClass('active').next('ul').slideToggle();
    $(this).parent().siblings().children('ul').slideUp();
    $(this).parent().siblings().children('.active').removeClass('active');
  });

  // Login Register tab
  $('.tab-menu').click(function () {
    $(".tab").removeClass('tab-active');
    $(".tab[data-id='" + $(this).attr('data-id') + "']").addClass("tab-active");
    $('.tab-menu').removeClass('active-menu');
    $(this).addClass('active-menu');
  });

  // Add Clearfix
  $('.footer-widget-blog .wp-block-latest-posts li').append('<div class="clearfix"></div>')

  // niceSelect
  $('select:not(.country_select,.state_select)').niceSelect();

  // wow animate 
  setTimeout(myGreeting, 1800);

  function myGreeting() {
    var wow = new WOW({
      boxClass: 'wow', // animated element css class (default is wow)
      animateClass: 'animated', // animation css class (default is animated)
      offset: 0, // distance to the element when triggering the animation (default is 0)
      mobile: true, // trigger animations on mobile devices (default is true)
      live: true, // act on asynchronously loaded content (default is true)
      callback: function (box) {
        // the callback is fired every time an animation is started
        // the argument that is passed in is the DOM node being animated
      },
      scrollContainer: null, // optional scroll container selector, otherwise use window,
      resetAnimation: true, // reset animation on end (default is true)
    });
    wow.init();
  }


  // mobile-search-area

  $('.search-btn').on("click", function () {
    $('.mobile-search').addClass('slide');
  });

  $('.search-cross-btn').on("click", function () {
    $('.mobile-search').removeClass('slide');
  });

  // scroll button
  $(window).on('scroll', function () {
    if ($(window).scrollTop() > 300) {
      $('.scroll-btn').addClass('show');
    } else {
      $('.scroll-btn').removeClass('show');
    }
  });
  $('.scroll-btn').on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: 0
    }, '300');
  });

  // mobile-menu

  $('.mobile-menu-btn').on("click", function () {
    $('.main-menu').addClass('show-menu');
  });

  $('.menu-close-btn').on("click", function () {
    $('.main-menu').removeClass('show-menu');
  });

  // mobile-drop-down
  $('.dropdown-icon').on('click', function () {
    $(this).toggleClass('active').next('ul').slideToggle();
    $(this).parent().siblings().children('ul').slideUp();
    $(this).parent().siblings().children('.active').removeClass('active');
  });

  // Menu Toggle button sidebar

  var toggleIcon = document.querySelectorAll('.sidebar-menu-icon')
  var closeIcon = document.querySelectorAll('.cross-icon')
  var searchWrap = document.querySelectorAll('.menu-toggle-btn-full-shape')

  toggleIcon.forEach((element) => {
    element.addEventListener('click', () => {
      document.querySelectorAll('.menu-toggle-btn-full-shape').forEach((el) => {
        el.classList.add('show-sidebar')
      })
    })
  })

  closeIcon.forEach((element) => {
    element.addEventListener('click', () => {
      document.querySelectorAll('.menu-toggle-btn-full-shape').forEach((el) => {
        el.classList.remove('show-sidebar')
      })
    })
  })

  window.onclick = function (event) {
    // Menu Toggle button sidebar
    searchWrap.forEach((el) => {
      if (event.target === el) {
        el.classList.remove('show-sidebar')
      }
    })
  }

  // Home-1 banner slider

  var heroSliderTwo = new Swiper('.banner1', {
    slidesPerView: 1,
    speed: 1500,
    loop: true,
    spaceBetween: 10,
    loop: true,
    centeredSlides: true,
    roundLengths: true,
    parallax: true,
    effect: 'fade',
    navigation: false,
    fadeEffect: {
      crossFade: true,
    },


    autoplay: {
      delay: 4000
    },
    pagination: {
      el: ".hero-one-pagination",
      clickable: true,

    }
  });


  // category1-slider

  var swiper = new Swiper(".category1-slider", {
    slidesPerView: 1,
    speed: 1000,
    spaceBetween: 30,
    loop: true,
    autoplay: true,
    roundLengths: true,
    navigation: {
      nextEl: '.category-prev1',
      prevEl: '.category-next1',
    },

    breakpoints: {
      280: {
        slidesPerView: 1
      },
      440: {
        slidesPerView: 2
      },
      576: {
        slidesPerView: 2
      },
      768: {
        slidesPerView: 3
      },
      992: {
        slidesPerView: 5
      },
      1200: {
        slidesPerView: 6
      },
      1400: {
        slidesPerView: 7
      },

    }

  });

  var swiper = new Swiper(".category2-slider", {
    slidesPerView: 1,
    speed: 1000,
    spaceBetween: 30,
    loop: true,
    autoplay: true,
    roundLengths: true,
    pagination: false,
    navigation: {
      nextEl: '.category-prev2',
      prevEl: '.category-next2',
    },

    breakpoints: {
      280: {
        slidesPerView: 1
      },
      380: {
        slidesPerView: 2
      },
      540: {
        slidesPerView: 3
      },
      576: {
        slidesPerView: 3
      },
      768: {
        slidesPerView: 4
      },
      992: {
        slidesPerView: 5
      },
      1200: {
        slidesPerView: 6
      },
      1400: {
        slidesPerView: 7
      },
    }
  });

  // coming-feature-slider1
  var swiper = new Swiper(".upcoming-slider", {
    slidesPerView: 1,
    speed: 1000,
    spaceBetween: 24,
    loop: true,
    roundLengths: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: 'true',
    },
    navigation: {
      nextEl: '.coming-prev1',
      prevEl: '.coming-next1',
    },

    breakpoints: {
      480: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1200: {
        slidesPerView: 3,
      },

    }

  });
  var swiper = new Swiper(".upcoming-slider2", {
    slidesPerView: 1,
    speed: 1000,
    spaceBetween: 24,
    loop: true,
    roundLengths: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: 'true',
    },
    navigation: {
      nextEl: '.coming-prev2',
      prevEl: '.coming-next2',
    },

    breakpoints: {
      480: {
        slidesPerView: 1,
        pagination: false
      },
      768: {
        slidesPerView: 2,
        pagination: false
      },
      1200: {
        slidesPerView: 3,
      },

    }
  });


  var swiper = new Swiper(".upcoming-slider3", {
    slidesPerView: 1,
    speed: 1000,
    spaceBetween: 24,
    loop: true,
    roundLengths: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: 'true',
    },
    navigation: {
      nextEl: '.coming-prev3',
      prevEl: '.coming-next3',
    },

    breakpoints: {
      480: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1200: {
        slidesPerView: 3,
      },

    }
  });




  // blog-slider-slider1

  var swiper = new Swiper(".blog-slider", {
    slidesPerView: 2,
    speed: 1000,
    spaceBetween: 24,
    loop: true,
    roundLengths: true,
    navigation: {
      nextEl: '.blog-prev1',
      prevEl: '.blog-next1',
    },

    breakpoints: {
      280: {
        slidesPerView: 1
      },
      480: {
        slidesPerView: 1
      },
      768: {
        slidesPerView: 2
      },
      992: {
        slidesPerView: 2
      },
      1200: {
        slidesPerView: 3
      },

    }

  });

  // testimonial-slider

  var swiper = new Swiper(".testimonial-slider", {
    slidesPerView: 1,
    speed: 1000,
    spaceBetween: 24,
    loop: true,
    roundLengths: true,
    navigation: {
      nextEl: '.testi-prev1',
      prevEl: '.testi-next1',
    },

    breakpoints: {
      280: {
        slidesPerView: 1
      },
      480: {
        slidesPerView: 1,
        autoplay: true,
      },
      768: {
        slidesPerView: 1
      },
      992: {
        slidesPerView: 2
      },
      1200: {
        slidesPerView: 3
      },

    }
  });
  var swiper = new Swiper(".testimonial-slider2", {
    slidesPerView: 1,
    speed: 1000,
    spaceBetween: 24,
    loop: true,
    roundLengths: true,
    navigation: {
      nextEl: '.testi-prev2',
      prevEl: '.testi-next2',
    },

    breakpoints: {
      280: {
        slidesPerView: 1
      },
      480: {
        slidesPerView: 1,
        autoplay: true,
      },
      768: {
        slidesPerView: 1
      },
      992: {
        slidesPerView: 2
      },
      1200: {
        slidesPerView: 3
      },

    }
  });

  // slick slider
  $('#slick1').slick({
    rows: 2,
    dots: true,
    arrows: false,
    infinite: true,
    speed: 300,
    slidesToShow: 6,
    slidesToScroll: 6,
    responsive: [{
        breakpoint: 1200,
        settings: {
          arrows: false,
          slidesToShow: 5
        }
      },
      {
        breakpoint: 991,
        settings: {
          arrows: false,
          slidesToShow: 4
        }
      },
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          slidesToShow: 3
        }
      },
      {
        breakpoint: 576,
        settings: {
          arrows: false,
          slidesToShow: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          slidesToShow: 2
        }
      },
      {
        breakpoint: 350,
        settings: {
          arrows: false,
          slidesToShow: 1
        }
      }
    ]
  });
  // timer start
  // Coming Soon Countdown 

  $('[data-countdown]').each(function () {
    var $deadline = new Date($(this).data('countdown')).getTime();

    var $dataDays = $(this).children('[data-days]');
    var $dataHours = $(this).children('[data-hours]');
    var $dataMinutes = $(this).children('[data-minutes]');
    var $dataSeconds = $(this).children('[data-seconds]');

    var x = setInterval(function () {

      var now = new Date().getTime();
      var t = $deadline - now;

      var days = Math.floor(t / (1000 * 60 * 60 * 24));
      var hours = Math.floor(t % (1000 * 60 * 60 * 24) / (1000 * 60 * 60));
      var minutes = Math.floor(t % (1000 * 60 * 60) / (1000 * 60));
      var seconds = Math.floor(t % (1000 * 60) / (1000));

      $dataDays.html(`${days}  <span>Days</span>`);
      $dataHours.html(`${hours}  <span>Hrs</span>`);
      $dataMinutes.html(`${minutes}  <span>Mins</span>`);
      $dataSeconds.html(`${seconds}  <span>Secs</span>`);

      if (t <= 0) {
        clearInterval(x);
        $dataDays.html('00');
        $dataHours.html('00');
        $dataMinutes.html('00');
        $dataSeconds.html('00');
      }

    }, 1000);
  })
  // timer end
  // Odometer Counter
  $(".counter-item").each(function () {
    $(this).isInViewport(function (status) {
      if (status === "entered") {
        for (var i = 0; i < document.querySelectorAll(".odometer").length; i++) {
          var el = document.querySelectorAll('.odometer')[i];
          el.innerHTML = el.getAttribute("data-odometer-final");
        }
      }
    });
  });

  $(".counter-single").each(function () {
    $(this).isInViewport(function (status) {
      if (status === "entered") {
        for (var i = 0; i < document.querySelectorAll(".odometer").length; i++) {
          var el = document.querySelectorAll('.odometer')[i];
          el.innerHTML = el.getAttribute("data-odometer-final");
        }
      }
    });
  });

  // Magnific Popup video
  $('.popup-youtube').magnificPopup({
    type: 'iframe'
  });

  // Quantity plus minus
  if( egns_theme_options.is_woocommerce ) {
    $(document).on( 'click', 'button.plus, button.minus', function() {

      if( egns_theme_options.is_cart ) {
        var min_qty =  1;
      }else if( egns_theme_options.is_product ) {
        var min_qty =  0;
      }
  
      var qty = $( this ).parent( '.quantity' ).find( '.qty' );
      var val = parseFloat(qty.val());
      var max = parseFloat(qty.attr( 'max' ));
      var min = parseFloat(qty.attr( 'min' ));
      var step = parseFloat(qty.attr( 'step' ));
      if ( $( this ).is( '.plus' ) ) {
        if ( max && ( max <= val ) ) {
          qty.val( max ).change();
        } else {
          qty.val( val + step ).change();
        }
      } else {
        if ( min && ( min >= val ) ) {
          qty.val( min ).change();
        } else if ( val > min_qty ) {
          qty.val( val - step ).change();
        }
    }})
  }
  

}(jQuery));