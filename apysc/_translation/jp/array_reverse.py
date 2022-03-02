"""This module is for the translation mapping data of the
following document:

Document file: array_reverse.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class reverse interface':
    '',

    'This page explains the `Array` class `reverse` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `reverse` method interface reverses an array\'s values order in place.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `reverse` method requires no arguments and returns no value.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 3, 5])\narr.reverse()\nassert arr == [5, 3, 1]\n```':  # noqa
    '',

    '':
    '',

    '## See also':
    '',

    '- [Array class sort interface](array_sort.md)':
    '',

    '## reverse API':
    '',

    '<!-- Docstring: apysc._type.array.Array.reverse -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `reverse(self) -> None`<hr>\n\n**[Interface summary]** Reverse this array in place.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.reverse()\n>>> arr\nArray([3, 2, 1])\n```':  # noqa
    '',

}
