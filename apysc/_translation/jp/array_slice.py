"""This module is for the translation mapping data of the
following document:

Document file: array_slice.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class slice interface':
    '',

    'This page explains the `Array` class `slice` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `slice` method interface extracts the specified index range array\'s values and returns a new array.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `slice` method requires the `start` and `end` arguments (`int` or `Int` values) and returns a new array.\n\nIf you specify 1 to the `start` argument and 3 to the `end` argument, this method behaves like the Python built-in list slice of `[1:3]`.\n\nAn original array is not modified.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3, 4])\nsliced_arr: ap.Array[int] = arr.slice(start=1, end=3)\nassert sliced_arr == [2, 3]\nassert arr == [1, 2, 3, 4]\n```':  # noqa
    '',

    '':
    '',

    '## slice API':
    '',

    '<!-- Docstring: apysc._type.array.Array.slice -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `slice(self, *, start:Union[int, apysc._type.int.Int, NoneType]=None, end:Union[int, apysc._type.int.Int, NoneType]=None) -> \'Array\'`<hr>\n\n**[Interface summary]** Slice this array by specified start and end indexes.<hr>\n\n**[Parameters]**\n\n- `start`: Int or int or None, default None\n  - Slicing start index.\n- `end`: Int or int or None, default None\n  - Slicing end index (a result array does not contain this index).\n\n<hr>\n\n**[Returns]**\n\n- `sliced_arr`: Array\n  - Sliced array.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3, 4])\n>>> arr.slice(start=1, end=3)\nArray([2, 3])\n\n>>> arr.slice(start=1)\nArray([2, 3, 4])\n\n>>> arr.slice(end=2)\nArray([1, 2])\n```':  # noqa
    '',

}
