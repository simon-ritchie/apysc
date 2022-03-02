"""This module is for the translation mapping data of the
following document:

Document file: display_object_get_and_set_css.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Display object get_css and set_css interfaces':
    '',

    'This page will explain the `DisplayObject` class `get_css` and `set_css` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `get_css` method will return a `css` string, and the `set_css` method will set the CSS setting to a `DisplayObject` instance.':  # noqa
    '',

    '## Basic usage':
    '',

    'Each interface requires the `name` argument as the CSS name. In addition, the `set_css` method interface also requires the `value` argument as the CSS value string.\n\nThe following example sets the `none` value to the `display` CSS if the current CSS value is the default (blank string, `\'\'`). Otherwise, revert the value to default (`Else` case) by the timer event (ticks every second).':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _SpriteOptions(TypedDict):\n    sprite: ap.Sprite\n\n\ndef on_timer(e: ap.TimerEvent, options: _SpriteOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = options[\'sprite\']\n    display_css_val: ap.String = sprite.get_css(name=\'display\')\n    condition: ap.Boolean = display_css_val == \'none\'\n    with ap.If(condition):\n        sprite.set_css(name=\'display\', value=\'\')\n    with ap.Else():\n        sprite.set_css(name=\'display\', value=\'none\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\noptions: _SpriteOptions = {\'sprite\': sprite}\ntimer: ap.Timer = ap.Timer(\n    handler=on_timer, delay=1000, options=options)\ntimer.start()\n\nap.save_overall_html(\n    dest_dir_path=\'display_object_get_and_set_css_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/display_object_get_and_set_css_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## get_css API':
    '',

    '<!-- Docstring: apysc._display.css_interface.CssInterface.get_css -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `get_css(self, name:Union[str, apysc._type.string.String]) -> apysc._type.string.String`<hr>\n\n**[Interface summary]** Get a CSS value string.<hr>\n\n**[Parameters]**\n\n- `name`: str or String\n  - CSS name (e.g., \'display\').\n\n<hr>\n\n**[Returns]**\n\n- `css`: ap.String\n  - CSS value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> sprite.set_css(name=\'display\', value=\'none\')\n>>> sprite.get_css(name=\'display\')\nString(\'none\')\n```':  # noqa
    '',

    '':
    '',

    '## set_css API':
    '',

    '<!-- Docstring: apysc._display.css_interface.CssInterface.set_css -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `set_css(self, name:Union[str, apysc._type.string.String], value:Union[str, apysc._type.string.String]) -> None`<hr>\n\n**[Interface summary]** Set a specified value string to the CSS.<hr>\n\n**[Parameters]**\n\n- `name`: str or String\n  - CSS name (e.g., \'display\').\n- `value`: str or String\n  - A CSS value string (e.g., \'none\').\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> sprite.set_css(name=\'display\', value=\'none\')\n>>> sprite.get_css(name=\'display\')\nString(\'none\')\n```':  # noqa
    '',

}
