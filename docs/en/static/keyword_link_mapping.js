
$(document).ready(function() {
    const KEYWORD_LINK_MAPPINGS = {"Stage": "https://simon-ritchie.github.io/apysc/en/stage.html", "Sprite": "https://simon-ritchie.github.io/apysc/en/sprite.html", "save_overall_html": "https://simon-ritchie.github.io/apysc/en/save_overall_html.html"};
    for (let keyword in KEYWORD_LINK_MAPPINGS) {
        let link = KEYWORD_LINK_MAPPINGS[keyword];
        $("span:contains(" + keyword + ")").each(function() {
            let elemText = $(this).text();
            elemText = sanitise(elemText);
            if (elemText !== keyword) {
                return;
            }
            let className = $(this).attr("class");
            className = sanitise(className);
            if (className !== "pre") {
                return;
            }
            $(this).html("<a href='" + link + "'>" + $(this).html() + "</a>");
        });
    }
});
