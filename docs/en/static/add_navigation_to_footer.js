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

    let href = sanitise($("[title='next chapter']").attr("href"));
    let linkText = sanitise(String($("[title='next chapter']").text()));
    if (linkText.trim() === "") {
        return;
    }
    $("div.body").append(
        '<br> Next topic: <a href="' + href + '">' + linkText + '</a>');
});
