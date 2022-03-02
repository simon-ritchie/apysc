"""This module is for the translation mapping data of the
following document:

Document file: append_js_expression.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# append_js_expression interface':
    '',

    'This page explains the `append_js_expression` function interface.':
    '',

    '## What interface is this?':
    '',

    'The `append_js_expression` function interface appends any JavaScript to the exported HTML at any position. This interface may be helpful if you need to use the apysc not supported interfaces or irregular JavaScript implementation, like the Django template tags or parameters (e.g., `{% if ... %}`).':  # noqa
    '',

    '## Basic usage':
    '',

    'The `append_js_expression` function requires JavaScript string at the argument.\n\nThe following example appends the `console.log` JavaScript calling at the rectangle click handler:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.append_js_expression(\n        expression=\'console.log("The rectangle is clicked!");\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'append_js_expression_basic_usage/\')\n```':  # noqa
    '',

    'If you click the following rectangle, the handler displays the `The rectangle is clicked!` message on the browser console (please press the F12 key).\n\n<iframe src="static/append_js_expression_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## append_js_expression API':
    '',

    '<!-- Docstring: apysc._expression.expression_data_util.append_js_expression -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `append_js_expression(expression:str) -> None`<hr>\n\n**[Interface summary]** Append js expression.<hr>\n\n**[Parameters]**\n\n- `expression`: str\n  - JavaScript Expression string.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> ap.append_js_expression(expression=\'console.log("Hello!")\')\n```':  # noqa
    '',

}
