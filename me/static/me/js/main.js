jQuery(document).ready(function($){
	//open-close submenu on mobile
	$('.main-nav').on('click', function(event){
		if($(event.target).is('.main-nav')) $(this).children('ul').toggleClass('is-visible');
	});

	$('#nav').scrollspy();

	
});

$(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});



