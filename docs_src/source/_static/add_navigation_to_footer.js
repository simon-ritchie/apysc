// The script to add a navigation links to the footer.

$(document).ready(function() {

    /**
     * Sanitise a specified text.
     * @param {String} text A target text to sanitise.
     * @returns {String} The sanitised text.
     */
    function sanitise(text) {
        text = text
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/'/g, '&#039;')
            .replace(/"/g, '&quot;');
        return text;
    }

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
