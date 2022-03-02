"""This module is for the translation mapping data of the
following document:

Document file: trace.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Trace interface':
    '',

    'This page explains the `trace` function interface.':
    '',

    '## What interface is this?':
    '',

    'The `trace` function interface displays any message on the browser console. This interface behaves like the JavaScript `console.log` function.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `trace` function can accept any number of arguments and various value types.\n\nThe following example draws the rectangle. Then, the handler displays the message on the browser console when you click it(please press the F12 key).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_rectangle_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'Hello apysc!\', \'Rectangle width:\', e.this.width)\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(\n    dest_dir_path=\'trace_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/trace_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## trace API':
    '',

    '<!-- Docstring: apysc._console._trace.trace -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `trace(*args:Any) -> None`<hr>\n\n**[Interface summary]** Display arguments information to console. This function saves a JavaScript `console.log` expression.<hr>\n\n**[Parameters]**\n\n- `*args`: list\n  - Any arguments to display to console.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.trace(\'Int value is:\', int_val)\n```':  # noqa
    '',

}
