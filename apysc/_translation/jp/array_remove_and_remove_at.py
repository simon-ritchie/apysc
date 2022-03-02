"""This module is for the translation mapping data of the
following document:

Document file: array_remove_and_remove_at.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class remove and remove_at interfaces':
    '',

    'This page explains the `Array` class `remove` and `remove_at` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `remove` method removes a specified value from an array, and the `remove_at` method removes a specified index value.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `remove` method requires target value at the first argument, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3])\narr.remove(value=2)\nassert arr == [1, 3]\n```':  # noqa
    '',

    'The `remove_at` method requires index (`int` or `Int` value) at the first argument, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3])\narr.remove_at(index=1)\nassert arr == [1, 3]\n```':  # noqa
    '',

    '':
    '',

    '## remove API':
    '',

    '<!-- Docstring: apysc._type.array.Array.remove -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `remove(self, value:~T) -> None`<hr>\n\n**[Interface summary]** Remove a specified value from this array.<hr>\n\n**[Parameters]**\n\n- `value`: Any\n  - Value to remove.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 3, 5])\n>>> arr.remove(3)\n>>> arr\nArray([1, 5])\n```':  # noqa
    '',

    '':
    '',

    '## remove_at API':
    '',

    '<!-- Docstring: apysc._type.array.Array.remove_at -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `remove_at(self, index:Union[int, apysc._type.int.Int]) -> None`<hr>\n\n**[Interface summary]** Remove a specified index value from this array.<hr>\n\n**[Parameters]**\n\n- `index`: Int or int\n  - Index to remove value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.remove_at(1)\n>>> arr\nArray([1, 3])\n```':  # noqa
    '',

}
