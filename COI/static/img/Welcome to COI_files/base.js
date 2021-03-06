
/*!
 * hoverIntent v1.8.0 // 2014.06.29 // jQuery v1.9.1+
 * http://cherne.net/brian/resources/jquery.hoverIntent.html
 *
 * You may use hoverIntent under the terms of the MIT license. Basically that
 * means you are free to use hoverIntent as long as this header is left intact.
 * Copyright 2007, 2014 Brian Cherne
 */
(function($){$.fn.hoverIntent=function(handlerIn,handlerOut,selector){var cfg={interval:100,sensitivity:6,timeout:0};if(typeof handlerIn==="object"){cfg=$.extend(cfg,handlerIn)}else{if($.isFunction(handlerOut)){cfg=$.extend(cfg,{over:handlerIn,out:handlerOut,selector:selector})}else{cfg=$.extend(cfg,{over:handlerIn,out:handlerIn,selector:handlerOut})}}var cX,cY,pX,pY;var track=function(ev){cX=ev.pageX;cY=ev.pageY};var compare=function(ev,ob){ob.hoverIntent_t=clearTimeout(ob.hoverIntent_t);if(Math.sqrt((pX-cX)*(pX-cX)+(pY-cY)*(pY-cY))<cfg.sensitivity){$(ob).off("mousemove.hoverIntent",track);ob.hoverIntent_s=true;return cfg.over.apply(ob,[ev])}else{pX=cX;pY=cY;ob.hoverIntent_t=setTimeout(function(){compare(ev,ob)},cfg.interval)}};var delay=function(ev,ob){ob.hoverIntent_t=clearTimeout(ob.hoverIntent_t);ob.hoverIntent_s=false;return cfg.out.apply(ob,[ev])};var handleHover=function(e){var ev=$.extend({},e);var ob=this;if(ob.hoverIntent_t){ob.hoverIntent_t=clearTimeout(ob.hoverIntent_t)}if(e.type==="mouseenter"){pX=ev.pageX;pY=ev.pageY;$(ob).on("mousemove.hoverIntent",track);if(!ob.hoverIntent_s){ob.hoverIntent_t=setTimeout(function(){compare(ev,ob)},cfg.interval)}}else{$(ob).off("mousemove.hoverIntent",track);if(ob.hoverIntent_s){ob.hoverIntent_t=setTimeout(function(){delay(ev,ob)},cfg.timeout)}}};return this.on({"mouseenter.hoverIntent":handleHover,"mouseleave.hoverIntent":handleHover},cfg.selector)}})(jQuery);



// function updateSliderSize() {
// 	var imgHeight = $(".slider_content").css("height");
// 	$(".lSSlideOuter").css("height", imgHeight);
// }

$(document).ready(function() {

	// $(window).on("resize", updateSliderSize);


	
	var config = {
		sensitivity: 3,
		interval: 300,
		over: function() { $(".menu_col").slideDown("800"); $("#main").animate({"margin-top": "+=15%"}, 350); $("#footer").animate({"margin-top": "+=15%"}, 350); },
		timeout: 150,
		out: function() { $(".menu_col").slideUp("800"); $("#main").animate({"margin-top": "-=15%"}, 350); $("#footer").animate({"margin-top": "-=15%"}, 350); },
	};
	$("#navbar_bottom").hoverIntent(config);





	$('#search_link').click(function() {
		$('#search_link').toggleClass("on_top");
		$('#search_link').toggleClass("transparent");

		$("#search_form").toggleClass("on_top");
		$("#search_form").toggleClass("transparent");
		
		
		$("#search_close").toggleClass("transparent");

		$('#search_form').animate({width: '+=160%'}, 1000, function(){});
		var height = $("#search_submit").css('height');
		$('#search_submit').css('width', height);
		// setTimeout(function() { $('#search_input').focus() }, 100);
	});

	$("#search_close a").click(function() {
		$("#search_close").toggleClass("transparent");

		$('#search_link').toggleClass("on_top");
		$('#search_link').toggleClass("transparent");
		
		$("#search_form").toggleClass("on_top");
		$("#search_form").toggleClass("transparent");
		

		$('#search_form').animate({width: '-=160%'}, 1000, function(){});
		var height = $("#search_submit").css('height');
		$('#search_submit').css('width', height);
	});






	config = {
		sensitivity: 1,
		interval: 0,
		over: function() { $(this).find(".slider_hidden").slideDown("0"); },
		timeout: 0,
		out: function() { $(this).find(".slider_hidden").slideUp("0"); },
	};
	$(".slider_visible").hoverIntent(config);


    var slider = $("#lightSlider").lightSlider({
    	item: 1,
    	mode: "slide",
    	useCSS: true,
    	cssEasing: 'ease',
    	easing: 'linear',
    	speed: 500,
    	slideMargin: 0,
    	loop: true,

    	controls: false,
    	pager: false,
    });
    



    $(".page").click(function(){
    	var i = $(this).index();

    	var activeBox = $("#slider_description .active");
    	var current_index = $('.pager .active').index();
    	if (i != current_index) {

    		$('.pager .active').each(function() {
    			$(this).removeClass("active");
    		});

    		activeBox.removeClass("active");
    		activeBox.addClass("hidden");
    	}


    	slider.goToSlide(i+1);


    	activeBox = $("#slider_description").children().eq(i);

    	if (i != current_index) {
    		$('.pager').each(function() {
    			$(this).children().eq(i).addClass("active");
    		});

    		activeBox.addClass("active");
    		activeBox.removeClass("hidden");
    	}

    });



});




