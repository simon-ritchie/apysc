"""This module is for the translation mapping data of the
following document:

Document file: for.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# For':
    '',

    'This page explains the `For` class.\n\nBefore reading on, maybe it is helpful to read the following page (the apysc uses the `For` class for the same reason for each data type):\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## What is the For class?':
    '',

    'The `For` class is the apysc for loop class. It behaves like the Python built-in `for` keyword.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `For` class requires using the `with` statement. The `as` keyword value becomes the `Int` type index (an `i` variable).\n\nThe following example draws the three rectangles in the `with For` block:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\narr: ap.Array[int] = ap.Array(range(3))\ni: ap.Int\nwith ap.For(arr) as i:\n    sprite.graphics.draw_rect(\n        x=i * 100 + 50, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'for_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/for_basic_usage/index.html" width="350" height="150"></iframe>\n\nThe `For` class constructor\'s first argument accepts an `Array` or `Dictionary` value. If you pass a `Dictionary` value, the `as` keyword value becomes a `String` value, not `Int`\\.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150,\n    background_color=\'#333\', stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\ndict_val: ap.Dictionary = ap.Dictionary(\n    {\'magenta\': ap.String(\'#f0a\'), \'cyan\': ap.String(\'#0af\')})\nkey: ap.String\nwith ap.For(dict_val) as key:\n    color: ap.String = dict_val[key]\n    sprite.graphics.begin_fill(color=color)\n    condition_1: ap.Boolean = key == \'magenta\'\n    condition_2: ap.Boolean = key == \'cyan\'\n    with ap.If(condition_1):\n        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n    with ap.Elif(condition_2):\n        sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'for_basic_usage_with_dict/\')\n```':  # noqa
    '',

    '<iframe src="static/for_basic_usage_with_dict/index.html" width="250" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [Each branch instruction class\'s scope variables reverting setting](branch_instruction_variables_reverting_setting.md)\n  - Notes: the `For` class also has the same arguments and behaves in the same way.':  # noqa
    '',

    '## For API':
    '',

    '<!-- Docstring: apysc._loop._for.For.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, arr_or_dict:Union[apysc._type.array.Array, apysc._type.dictionary.Dictionary], *, locals_:Union[Dict[str, Any], NoneType]=None, globals_:Union[Dict[str, Any], NoneType]=None) -> None`<hr>\n\n**[Interface summary]** A class to append for the (loop) expression.<hr>\n\n**[Parameters]**\n\n- `arr_or_dict`: Array or Dictionary\n  - Array or Dictionary instance to iterate.\n- `locals_`: dict or None, default None\n  - Current scope\'s local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameInterface variables (like Int, Sprite) at the end of a `For` scope. This setting is useful when you don\'t want to update each variable by implementing the `For` scope.\n- `globals_`: dict or None, default None\n  - Current scope\'s global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array(range(3))\n>>> with ap.For(arr) as i:\n...     ap.trace(\'Loop index is:\', i)\n```':  # noqa
    '',

}
