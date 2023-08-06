"""Enum class implementation for the easing setting.
"""

from enum import Enum


class Easing(Enum):
    """
    Enum class for the easing setting.

    References
    ----------
    - Easing enum
        - https://simon-ritchie.github.io/apysc/en/easing_enum.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50
    ... )
    >>> _ = rectangle.animation_y(
    ...     y=100,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... ).start()
    """

    LINEAR = "function(x) {return x;}"

    EASE_IN_SINE = "function(x) {return 1 - Math.cos((x * Math.PI) / 2);}"
    EASE_OUT_SINE = "function(x) {return Math.sin((x * Math.PI) / 2);}"
    EASE_IN_OUT_SINE = "function(x) {return -(Math.cos(Math.PI * x) - 1) / 2;}"

    EASE_IN_QUAD = "function(x) {return x * x;}"
    EASE_OUT_QUAD = "function(x) {return 1 - (1 - x) * (1 - x);}"
    EASE_IN_OUT_QUAD = (
        "function(x) {return x < 0.5 ? 2 * x * x " ": 1 - Math.pow(-2 * x + 2, 2) / 2;}"
    )

    EASE_IN_CUBIC = "function(x) {return x * x * x;}"
    EASE_OUT_CUBIC = "function(x) {return 1 - Math.pow(1 - x, 3);}"
    EASE_IN_OUT_CUBIC = (
        "function(x) {return x < 0.5 ? 4 * x * x * x "
        ": 1 - Math.pow(-2 * x + 2, 3) / 2;}"
    )

    EASE_IN_QUART = "function(x) {return x * x * x * x;}"
    EASE_OUT_QUART = "function(x) {return 1 - Math.pow(1 - x, 4);}"
    EASE_IN_OUT_QUART = (
        "function(x) {return x < 0.5 ? 8 * x * x * x * x "
        ": 1 - Math.pow(-2 * x + 2, 4) / 2;}"
    )

    EASE_IN_QUINT = "function(x) {return x * x * x * x * x;}"
    EASE_OUT_QUINT = "function(x) {return 1 - Math.pow(1 - x, 5);}"
    EASE_IN_OUT_QUINT = (
        "function(x) {return x < 0.5 ? 16 * x * x * x * x * x "
        ": 1 - Math.pow(-2 * x + 2, 5) / 2;}"
    )

    EASE_IN_EXPO = "function(x) {return x === 0 ? 0 " ": Math.pow(2, 10 * x - 10);}"
    EASE_OUT_EXPO = "function(x) {return x === 1 ? 1 " ": 1 - Math.pow(2, -10 * x);}"
    EASE_IN_OUT_EXPO = (
        "function(x) {return x === 0 ? 0 "
        ": x === 1 ? 1 "
        ": x < 0.5 ? Math.pow(2, 20 * x - 10) / 2 "
        ": (2 - Math.pow(2, -20 * x + 10)) / 2;}"
    )

    EASE_IN_CIRC = "function(x) {return 1 - Math.sqrt(1 - Math.pow(x, 2));}"
    EASE_OUT_CIRC = "function(x) {return Math.sqrt(1 - Math.pow(x - 1, 2));}"
    EASE_IN_OUT_CIRC = (
        "function(x) {return x < 0.5 "
        "? (1 - Math.sqrt(1 - Math.pow(2 * x, 2))) / 2 "
        ": (Math.sqrt(1 - Math.pow(-2 * x + 2, 2)) + 1) / 2;}"
    )

    EASE_IN_BACK = "function(x) {return 2.70158 * x * x * x - 1.70158 * x * x;}"
    EASE_OUT_BACK = (
        "function(x) {return 1 + 2.70158 * Math.pow(x - 1, 3) "
        "+ 1.70158 * Math.pow(x - 1, 2);}"
    )
    EASE_IN_OUT_BACK = (
        "function(x) {return x < 0.5 "
        "? (Math.pow(2 * x, 2) * ((2.5949095 + 1) * 2 * x - 2.5949095)) / 2 "
        ": (Math.pow(2 * x - 2, 2) * ((2.5949095 + 1) "
        "* (x * 2 - 2) + 2.5949095) + 2) / 2;}"
    )

    EASE_IN_ELASTIC = (
        "function(x) {return x === 0 ? 0 "
        ": x === 1 ? 1 "
        ": -Math.pow(2, 10 * x - 10) * Math.sin((x * 10 - 10.75) "
        "* ((2 * Math.PI) / 3));}"
    )
    EASE_OUT_ELASTIC = (
        "function(x) {return x === 0 ? 0 "
        ": x === 1 ? 1 "
        ": Math.pow(2, -10 * x) * Math.sin((x * 10 - 0.75) "
        "* ((2 * Math.PI) / 3)) + 1;}"
    )
    EASE_IN_OUT_ELASTIC = (
        "function(x) {return x === 0 ? 0 "
        ": x === 1 ? 1 "
        ": x < 0.5 ? -(Math.pow(2, 20 * x - 10) "
        "* Math.sin((20 * x - 11.125) * ((2 * Math.PI) / 4.5))) / 2 "
        ": (Math.pow(2, -20 * x + 10) * Math.sin((20 * x - 11.125) "
        "* ((2 * Math.PI) / 4.5))) / 2 + 1;}"
    )

    EASE_IN_BOUNCE = (
        "function(x) {function ease_out_bounce(y) {"
        "if (y < 1 / 2.75) {return 7.5625 * y * y;} "
        "else if (y < 2 / 2.75) {"
        "return 7.5625 * (y -= 1.5 / 2.75) * y + 0.75;} "
        "else if (y < 2.5 / 2.75) {"
        "return 7.5625 * (y -= 2.25 / 2.75) * y + 0.9375;} "
        "else {return 7.5625 * (y -= 2.625 / 2.75) * y + 0.984375;}} "
        "return 1 - ease_out_bounce(1 - x);}"
    )
    EASE_OUT_BOUNCE = (
        "function(x) {if (x < 1 / 2.75) {return 7.5625 * x * x;} "
        "else if (x < 2 / 2.75) {"
        "return 7.5625 * (x -= 1.5 / 2.75) * x + 0.75;} "
        "else if (x < 2.5 / 2.75) {"
        "return 7.5625 * (x -= 2.25 / 2.75) * x + 0.9375;} "
        "else {return 7.5625 * (x -= 2.625 / 2.75) * x + 0.984375;}}"
    )
    EASE_IN_OUT_BOUNCE = (
        "function(x) {function ease_out_bounce(y) {"
        "if (y < 1 / 2.75) {return 7.5625 * y * y;} "
        "else if (y < 2 / 2.75) {"
        "return 7.5625 * (y -= 1.5 / 2.75) * y + 0.75;} "
        "else if (y < 2.5 / 2.75) {"
        "return 7.5625 * (y -= 2.25 / 2.75) * y + 0.9375;} "
        "else {return 7.5625 * (y -= 2.625 / 2.75) * y + 0.984375;}} "
        "return x < 0.5 ? (1 - ease_out_bounce(1 - 2 * x)) / 2 "
        ": (1 + ease_out_bounce(2 * x - 1)) / 2;}"
    )
