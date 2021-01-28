/* global screenReaderText */
/**
 * Theme functions file.
 *
 * Contains handlers for navigation and widget area.
 */

( function( $ ) {
  var body, masthead, menuToggle, siteNavigation, siteHeaderMenu;

  function initMainNavigation( container ) {
    var screenReaderText = $('.screen-reader-text');

    // Add dropdown toggle that displays child menu items.
    var dropdownToggle = $( '<button />', {
      'class': 'dropdown-toggle',
      'aria-expanded': false
    } ).append( $( '<span />', {
      'class': 'screen-reader-text',
      text: screenReaderText.expand
    } ) );

    container.find( '.menu-item-has-children > a' ).after( dropdownToggle );

    // Toggle buttons and submenu items with active children menu items.
    container.find( '.current-menu-ancestor > button' ).addClass( 'toggled-on' );
    container.find( '.current-menu-ancestor > .sub-menu' ).addClass( 'toggled-on' );

    // Add menu items with submenus to aria-haspopup="true".
    container.find( '.menu-item-has-children' ).attr( 'aria-haspopup', 'true' );

    container.find( '.dropdown-toggle' ).click( function( e ) {
      var _this            = $( this ),
        screenReaderSpan = _this.find( '.screen-reader-text' );

      e.preventDefault();
      _this.toggleClass( 'toggled-on' );
      _this.next( '.children, .sub-menu' ).toggleClass( 'toggled-on' );

      // jscs:disable
      _this.attr( 'aria-expanded', _this.attr( 'aria-expanded' ) === 'false' ? 'true' : 'false' );
      // jscs:enable
      screenReaderSpan.text( screenReaderSpan.text() === screenReaderText.expand ? screenReaderText.collapse : screenReaderText.expand );
    } );
  }
  initMainNavigation( $( '.main-navigation' ) );

  masthead         = $( '#masthead' );  
  menuToggle       = masthead.find( '#menu-toggle' );
  siteHeaderMenu   = masthead.find( '#site-header-menu' );
  siteNavigation   = masthead.find( '#site-navigation' );

  fixedhead         = $( '#fixedhead' );
  menuToggleFixed       = fixedhead.find( '#menu-toggle-fixed' );
  siteHeaderMenuFixed   = fixedhead.find( '#site-header-menu-fixed' );
  siteNavigationFixed   = fixedhead.find( '#site-navigation-fixed' );
  // Enable menuToggle.
  ( function() {

    // Return early if menuToggle is missing.
    if ( ! menuToggle.length ) {
      return;
    }
    if ( ! menuToggleFixed.length ) {
      return;
    }

    // Add an initial values for the attribute.

    menuToggle.on( 'click', function() {
      $( this ).add( siteHeaderMenu ).toggleClass( 'toggled-on' );
    } );

    menuToggleFixed.on( 'click', function() {
      $( this ).add( siteHeaderMenuFixed ).toggleClass( 'toggled-on' );
    } );

  } )();

  // Fix sub-menus for touch devices and better focus for hidden submenu items for accessibility.
  ( function() {
    if ( ! siteNavigation.length || ! siteNavigation.children().length ) {
      return;
    }

    // Toggle `focus` class to allow submenu access on tablets.
    function toggleFocusClassTouchScreen() {
      if ( window.innerWidth >= 1200 ) {
        $( document.body ).on( 'touchstart', function( e ) {
          if ( ! $( e.target ).closest( '.main-navigation li' ).length ) {
            $( '.main-navigation li' ).removeClass( 'focus' );
          }
        } );
        siteNavigation.find( '.menu-item-has-children > a' ).on( 'touchstart', function( e ) {
          var el = $( this ).parent( 'li' );

          if ( ! el.hasClass( 'focus' ) ) {
            e.preventDefault();
            el.toggleClass( 'focus' );
            el.siblings( '.focus' ).removeClass( 'focus' );
          }
        } );
      } else {
        siteNavigation.find( '.menu-item-has-children > a' ).unbind( 'touchstart' );
      }
    }

    if ( 'ontouchstart' in window ) {
      $( window ).on( 'resize', toggleFocusClassTouchScreen );
      toggleFocusClassTouchScreen();
    }

    siteNavigation.find( 'a' ).on( 'focus blur', function() {
      $( this ).parents( '.menu-item' ).toggleClass( 'focus' );
    } );
  } )();

  // Add the default ARIA attributes for the menu toggle and the navigations.
  function onResizeARIA() {
    if ( window.innerWidth < 1200 ) {
      if ( menuToggle.hasClass( 'toggled-on' ) ) {
        menuToggle.attr( 'aria-expanded', 'true' );
      } else {
        menuToggle.attr( 'aria-expanded', 'false' );
      }

      if ( siteHeaderMenu.hasClass( 'toggled-on' ) ) {
        siteNavigation.attr( 'aria-expanded', 'true' );
      } else {
        siteNavigation.attr( 'aria-expanded', 'false' );
      }

      menuToggle.attr( 'aria-controls', 'site-navigation social-navigation' );
    } else {
      menuToggle.removeAttr( 'aria-expanded' );
      siteNavigation.removeAttr( 'aria-expanded' );
      menuToggle.removeAttr( 'aria-controls' );
    }
  }
  
} )( jQuery );