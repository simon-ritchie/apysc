// The common functions' definitions.

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
