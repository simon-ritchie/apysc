// The script to hide the headings and sidemenu's table
// of contents list.

$(document).ready(function() {
    $("h3:contains(Table of contents)").css("display", "none");
    $("div.sphinxsidebar a:contains(Table of contents)").parent().css(
        "display", "none");
});
