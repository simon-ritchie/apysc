// The script to hide the sidemenu's table of contents list.

$(document).ready(function() {
    $("div.sphinxsidebar a:contains(Table of contents)").parent().css(
        "display", "none");
});
