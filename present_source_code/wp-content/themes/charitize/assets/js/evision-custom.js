// On Document Load
jQuery(window).load(function(){
    //site loader
    jQuery('#wraploader').hide();
});

// On Document Ready
jQuery(document).ready(function ($) {

    // Main Slider
    var config = {
      fx : "fade",
      timeout : 7000,
      prev : "#charitize-prev",
      next : "#charitize-next",
      pager : "#charitize-pager",
      slides : "> div"
    };
    config['pause-on-hover'] = "true";

    $('#cycle-slideshow').cycle( config );

    // Carousel Slider
    
    config.carouselVisible = '3';
    config.prev = '#charitize-prev2'
    $('#cycle-carousel').cycle(config);
    
    /*wow jQuery*/
    wow = new WOW({
            boxClass: 'evision-animate'
        }
    )

    wow.init();

    // slick jQuery 
    jQuery('.carousel-group').slick({
      autoplay: true,
      autoplaySpeed: 3000,
      dots: true,
      slidesToShow: 4,
      slidesToScroll: 1,
      lazyLoad: 'ondemand',
      responsive: [
         {
           breakpoint: 1024,
           settings: {
             slidesToShow: 3,
             slidesToScroll: 3,
             infinite: true,
             dots: true
           }
         },
         {
           breakpoint: 768,
           settings: {
             slidesToShow: 2,
             slidesToScroll: 2
           }
         },
         {
           breakpoint: 481,
           settings: {
             slidesToShow: 1,
             slidesToScroll: 1
           }
         }
         // You can unslick at a given breakpoint now by adding:
         // settings: "unslick"
         // instead of a settings object
       ]
    });

    // back to top animation

    $('#gotop').click(function(){
      $('html,body').animate({scrollTop: '0px'},1000);
    });

    // waypoints
    if ( $('html,body').hasClass('home') && $('.wrapper-callback').length > 0 ) {
      var waypoint = new Waypoint({
        element: $('.wrapper-callback'),
        offset: '0',
        handler: function(direction) {
          $(window).scroll(function(){
            var scrolledY = $(window).scrollTop();
            $('.wrapper-callback').css('background-position', 'left ' + (-(scrolledY))/8 + 'px');
          });
        } 
      });
    }
    
    // header fix
    var initialPosition = $(window).scrollTop();
    $(window).scroll(function() {
      var getScrollTop = $('html,body').scrollTop(),
          mastheadHeight = $('#masthead').outerHeight(),
          headerFixed = $('#fixedhead');

        // console.log(mastheadHeight, 'hhhhe');

          
      if (getScrollTop > initialPosition) {
        $( '#fixedhead' ).css({'top': 0});
      } else {
        $( '#fixedhead' ).css({'top': - mastheadHeight});
      }

      if ( getScrollTop == 0 ) { 
       $( '#fixedhead' ).css({'top': - mastheadHeight});
      }
      initialPosition = getScrollTop;

      // back to top button visible on scroll
      var scrollTopPosition = $('html,body').scrollTop();
      if( scrollTopPosition > 240 ) {
        $('#gotop').css({'bottom': 25});
      } else {
        $('#gotop').css({'bottom': -100});
      }

      $('header#fixedhead').css('display', 'block');
    });

    $('header#fixedhead').css('display', 'none');

    // margin top social
    var mastheadHeight = $('#masthead').outerHeight(),
        mobileScreen = $(window).width();
        mobileScreenMargin(mobileScreen);

    function mobileScreenMargin(mobileScreen){
      if( mobileScreen >= 768 ){
        $('.evision-social-section').css('margin-top', mastheadHeight);
      }   else {
        $('.evision-social-section').css('margin-top', '0px');   
      }
    }


    // resize
    $(window).resize(function(){
       var  mastheadHeight = $('#masthead').outerHeight(),
            mobileScreen = $(window).width();
          $( '#fixedhead' ).css({'width': mobileScreen });
          mobileScreenMargin(mobileScreen);
    });
});