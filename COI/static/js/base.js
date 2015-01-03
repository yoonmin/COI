
$(document).ready(function() {

	updateSize();

	$(window).on("resize", updateSize);
	function updateSize() {
		$('#search_submit').css('width', $('#search_submit').height());
		$('#search_submit').css('margin-right', $('#search_submit').height()*0.4);
	}



	$('#navbar_menu > div > a').click(function() { 
		$('#navbar_hidden').slideToggle();
		$('#navbar_menu > div > a').toggleClass("transparent");
		$('#navbar_menu > div > a').toggleClass("on_top");

		$('#navbar_close > div > a').toggleClass("transparent");
		$('#navbar_close > div > a').toggleClass("on_top");
	});


	$('#navbar_close').click(function() { 
		$('#navbar_hidden').slideToggle();
		
		$('#navbar_menu > div > a').toggleClass("transparent");
		$('#navbar_menu > div > a').toggleClass("on_top");
		
		$('#navbar_close > div > a').toggleClass("transparent");
		$('#navbar_close > div > a').toggleClass("on_top");
	});	







	$('#search_link').click(function() {
		$('#search_link').toggleClass("transparent");
		$('#search_link').toggleClass("on_top");

		$("#search_form").toggleClass("transparent");
		$("#search_form").toggleClass("on_top");
		
		$("#search_close").toggleClass("transparent");

		$('#search_form').animate({width: '60%'}, 1000, function(){});
		setTimeout(function() { $('#search_input').focus() }, 100);
	});


	$("#search_close a").click(function() {
		$("#search_close").toggleClass("transparent");

		$('#search_link').toggleClass("transparent");
		$('#search_link').toggleClass("on_top");

		$("#search_form").toggleClass("transparent");
		$("#search_form").toggleClass("on_top");

		$('#search_form').animate({width: '15%'}, 1000, function(){});
	});




    var slider = $("#lightSlider").lightSlider({
    	item: 1,
    	mode: "slide",
    	useCSS: true,
    	cssEasing: 'ease',
    	easing: 'linear',
    	speed: 500,
    	slideMargin: 0,
    	loop: true,

    	controls: true,
    	prevHtml: '',
    	nextHtml: '',
    	
    	pager: true,
    });
    



    $("#news_col a").click(function() {
    	var i = $(this).index();

    	var active = $('#news_description .active');
    	var current_index = active.index();
    	if (i != current_index) {
    		$("#news_col .active").removeClass("active");
    		active.animate({'right': '5000px'}, 500, function(){});
    		active.attr('class', 'hidden');
    	}

    	slider.goToSlide(i+1);

    	active = $('#news_description').children().eq(i);
    	if (i != current_index) {
    		$('#news_col').children().eq(i).find('li').addClass('active');
    		active.animate({'right': '0'}, 500, function(){});
    		active.attr('class', 'active');
    	}


    });
})




