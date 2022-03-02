"""This module is for the translation mapping data of the
following document:

Document file: array_sort.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class sort interface':
    '',

    'This page explains the `Array` class `sort` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `sort` method interface sorts an array\'s values (ascending order).':  # noqa
    '',

    '## Basic usage':
    '',

    'The `sort` method requires no arguments and sorts values in place (no return value).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([5, 1, 3])\narr.sort()\nassert arr == [1, 3, 5]\n```':  # noqa
    '',

    '':
    '',

    '## Sort values by descending order':
    '',

    'If you need to sort values by descending order, then use the `reverse` method also:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 3, 2])\narr.sort()\narr.reverse()\nassert arr == [3, 2, 1]\n```':  # noqa
    '',

    '':
    '',

    '## See also':
    '',

    '- [Array class reverse interface](array_reverse.md)':
    '',

    '## sort API':
    '',

    '<!-- Docstring: apysc._type.array.Array.sort -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `sort(self, *, ascending:bool=True) -> None`<hr>\n\n**[Interface summary]** Sort this array in place.<hr>\n\n**[Parameters]**\n\n- `ascending`: bool, default True\n  - Sort by ascending or not. If False is specified, this interface sorts values descending.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([3, 5, 1, 4, 2])\n>>> arr.sort()\n>>> arr\nArray([1, 2, 3, 4, 5])\n\n>>> arr.sort(ascending=False)\n>>> arr\nArray([5, 4, 3, 2, 1])\n```':  # noqa
    '',

}
