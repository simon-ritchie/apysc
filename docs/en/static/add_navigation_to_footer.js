// The script to add a navigation links to the footer.

$(document).ready(function() {

    let href = $("[title='next chapter']").attr("href");
    let linkText = String($("[title='next chapter']").text());
    if (linkText.trim() === "") {
        return;
    }
    href = sanitise(href);
    linkText = sanitise(linkText);
    $("div.body").append(
        '<br> Next topic: <a href="' + href + '">' + linkText + '</a>');
});
