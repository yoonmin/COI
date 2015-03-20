var originalHtml = $(".menubar_tabbed_content").html();
var originalPaper = $("#paper_result").html();

$(document).ready(function() {
    $("#people_input").keydown(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });
    $("#people_input").keyup(search_people);



    $("#title_input").keydown(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });
    $("#title_input").keyup(search_title);


    $("#author_input").keydown(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });
    $("#author_input").keyup(search_author);
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


function search_title(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
        return false;
    }
    else {
        if (event.keyCode == 27) {
            $("#title_input").val("");
        }

        var regex = new RegExp("^[a-zA-Z0-9]*$");
        var query = $("#title_input").val();

        if (regex.test(query)) {
            if (query.length >= 2) {
                $("#paper_result").html("<div class=\"loading_img\"></div>");
                $.get(document.URL, {'title': query}, function(data) {
                    $("#paper_result").html(data);
                });
            }
            else if (query.length <= 1) {
                $("#paper_result").html(originalPaper);
            }
        }
    }
}

function search_author(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
        return false;
    }

    else {
        if (event.keyCode == 27) {
            $("#author_input").val("");
        }

        var regex = new RegExp("^[a-zA-Z0-9]*$");
        var query = $("#author_input").val();

        if (regex.test(query)) {
            if (query.length >= 2) {
                $("#paper_result").html("<div class=\"loading_img\"></div>");
                $.get(document.URL, {'author': query}, function(data) {
                    $("#paper_result").html(data);
                });
            }
            else if (query.length <= 1) {
                $("#paper_result").html(originalPaper);
            }
        }
    }
}








