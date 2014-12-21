$(document).ready(function() {
    $("#navigator_content_user_profile").hover(
        function() {
            $(".toggle_profile_menu_down").attr("class", "toggle_profile_menu_up");
            $("#profile_menu_option_list").show();
        },
        function() {
            $(".toggle_profile_menu_up").attr("class", "toggle_profile_menu_down");
            $("#profile_menu_option_list").hide();
        }
    );
});