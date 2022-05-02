// The script to add a navigation links to the footer.

$(document).ready(function() {
    let href = $("[title='next chapter']").attr("href");
    let linkText = $("[title='next chapter']").text();
    $("div.body").append(
        '<br>Next topic: <a href="' + href + '">' + linkText + '</a>');
});
