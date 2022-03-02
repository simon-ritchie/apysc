"""This module is for the translation mapping data of the
following document:

Document file: array_index_of.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class index_of interface':
    '',

    'This page explains the `Array` class `index_of` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `index_of` method returns the specified value\'s index in the array.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `index_of` method requires the `value` argument and returns the found value\'s index in the array.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 3, 5])\nindex: ap.Int = arr.index_of(value=3)\nassert index == 1\n```':  # noqa
    '',

    'If there is no found value, the return index becomes `-1`.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 3, 5])\nindex: ap.Int = arr.index_of(value=2)\nassert index == -1\n```':  # noqa
    '',

    '':
    '',

    '## index_of API':
    '',

    '<!-- Docstring: apysc._type.array.Array.index_of -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `index_of(self, value:~T) -> apysc._type.int.Int`<hr>\n\n**[Interface summary]** Search specified value\'s index and return it.<hr>\n\n**[Parameters]**\n\n- `value`: *\n  - Any value to search.\n\n<hr>\n\n**[Returns]**\n\n- `index`: Int\n  - Found position of index. If this array does not contain a value, this interface returns -1.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 3, 5])\n>>> arr.index_of(3)\nInt(1)\n```':  # noqa
    '',

}
