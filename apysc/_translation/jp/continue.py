"""This module is for the translation mapping data of the
following document:

Document file: continue.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Continue':
    '',

    'This page explains the `Continue` class.\n\nBefore reading on, maybe it is helpful to read the following page (apysc uses the `Continue` class for the same reason):\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## What is the Continue class?':
    '',

    'The `with For` block uses the `Continue` class to skip a current loop iteration (in JavaScript). It behaves like the Python built-in `continue` keyword.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `Continue` class can only be used in the `with For` (or other loop class) block, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\narr: ap.Array = ap.Array(range(2))\ni: ap.Int\nwith ap.For(arr) as i:\n    condition: ap.Boolean = i == 0\n    with ap.If(condition):\n        sprite.graphics.begin_fill(color=\'#0af\')\n        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n        ap.Continue()\n\n    sprite.graphics.begin_fill(color=\'#f0a\')\n    sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'continue_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/continue_basic_usage/index.html" width="250" height="150"></iframe>\n\nIf you use the `Continue` class in the out of the `with For` block, then an exception is raised:':  # noqa
    '',

    '```py\nimport apysc as ap\n\nap.Continue()\n```':
    '',

    '':
    '',

    '```\nException: The `Continue` class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.\n```':  # noqa
    '',

    '':
    '',

    '## Continue API':
    '',

    '<!-- Docstring: apysc._loop._continue.Continue.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self) -> None`<hr>\n\n**[Interface summary]** The loop continue expression class.<hr>\n\n**[Notes]**\n\nThis class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array(range(3))\n>>> with ap.For(arr) as i:\n...     with ap.If(i == 1):\n...         _ = ap.Continue()\n```':  # noqa
    '',

}
