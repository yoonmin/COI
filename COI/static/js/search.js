var originalHtml = $(".menubar_tabbed_content").html();

$(document).ready(function() {
    $("#people_input").keydown(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });
    $("#people_input").keyup(search_people);
});

function search_people(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
        return false;
    }

    else {
        if (event.keyCode == 27) {
            $("#people_input").val("");
        }

        var regex = new RegExp("^[a-zA-Z0-9]*$");
        var query = $("#people_input").val();

        if (regex.test(query)) {
            if (query.length >= 2) {
                $(".menubar_tabbed_menu").addClass("transparent");
                $(".menubar_tabbed_content").html("<div class=\"loading_img\"></div>");
                $.get(document.URL, {'q': query}, function(data) {
                    $(".menubar_tabbed_content").html(data);
                });
            }
            else if (query.length <= 1) {
                $(".menubar_tabbed_menu").removeClass("transparent");
                $(".menubar_tabbed_content").html(originalHtml);
            }
        }
    
    }


}
