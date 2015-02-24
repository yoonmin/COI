function nl2br(str, is_xhtml) {
	var breakTag = (is_xhtml || typeof is_xhtml === 'undefined') ? '<br />' : '<br>';
	return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
}

$(".menubar_tab").click(function() {
	var category = $(this).data("tab");

	$(".menubar_tabbed_content").html("<div class=\"loading_img\"></div>");

	$(".current").removeClass("current");
	$(this).addClass("current");

	$.get(
		document.URL, 
		{"category": category},
		function(data) {
			$(".menubar_tabbed_content").html(data);
		}
	);
});