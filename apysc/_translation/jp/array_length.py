"""This module is for the translation mapping data of the
following document:

Document file: array_length.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class length interface':
    '',

    'This page explains the `Array` class `length` property interface.':
    '',

    '## What interface is this?':
    '',

    'The `length` attribute interface returns a current array\'s values length.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `length` property has the only getter interface. The return value type is the `Int` type.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3, 4])\nlength: ap.Int = arr.length\nassert length == 4\n```':  # noqa
    '',

    '':
    '',

    '## Notes of the len() function':
    '',

    'The `Array` class is not supported the Python built-in `len()` function, and its function raises an exception. Please use the `length` property instead.':  # noqa
    '',

    '```py\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3, 4])\nlen(arr)\n```':  # noqa
    '',

    '':
    '',

    '```\nException: Array instance can\'t apply len function. Please use length property instead.\n```':  # noqa
    '',

    '':
    '',

    '## length property API':
    '',

    '<!-- Docstring: apysc._type.array.Array.length -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get length of this array.<hr>\n\n**[Returns]**\n\n- `length`: Int\n  - This array\'s length.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.length\nInt(3)\n```':  # noqa
    '',

}
