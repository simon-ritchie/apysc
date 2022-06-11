// The script to add a Japanese translated document's link
// from an English language document.

$(document).ready(function() {

    const LANGUAGE = window.navigator.language;

    if (LANGUAGE !== "ja") {
        return;
    }

    const ORIGINAL_FILE_NAME = window.location.href.split("/").pop();
    let href = window.location.href;
    href = href.replace("/en/", "/jp/");
    href = href.replace(ORIGINAL_FILE_NAME, "jp_" + ORIGINAL_FILE_NAME);
    href = sanitise(href);

    $("div.body").prepend(
        '※この資料には<a href="' + href + '">日本語の翻訳版</a>が存在します。<br><br>'
    );
});
