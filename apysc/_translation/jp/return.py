"""This module is for the translation mapping data of the
following document:

Document file: return.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Return':
    '',

    'This page explains the `Return` class.\n\nBefore reading on, maybe it is helpful to read the following page (the apysc uses the `Return` class for the same reason of each apysc data type):\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## What is the Return class?':
    '',

    'The `Return` class behaves to append the `return;` JavaScript code. Therefore, this class can be used only in an event handler (function or method) scope.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `Return` class constructor accepts no arguments. You can use this interface with the branch condition, for example, the `ap.If` class.\n\nThe following example changes the rectangle fill color when you click it. Each `ap.If` branch instantiate `Return` class, so the code applies the changing of fill color one by one:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    fill_color: ap.String = rectangle.fill_color\n    with ap.If(fill_color == \'#00aaff\'):\n        rectangle.fill_color = ap.String(\'#ff00aa\')\n        ap.Return()\n    with ap.If(fill_color == \'#ff00aa\'):\n        rectangle.fill_color = ap.String(\'#00ffaa\')\n        ap.Return()\n    with ap.If(fill_color == \'#00ffaa\'):\n        rectangle.fill_color = ap.String(\'#00aaff\')\n        ap.Return()\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#00aaff\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'return_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/return_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Return API':
    '',

    '<!-- Docstring: apysc._type._return.Return.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self) -> None`<hr>\n\n**[Interface summary]** Class for the return expression.<hr>\n\n**[Notes]**\n\nThis class can be instantiated only in an event handler scope.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:\n...     """\n...     The handler that the timer calls.\n...\n```':  # noqa
    '',

}
