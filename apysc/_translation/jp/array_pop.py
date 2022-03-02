"""This module is for the translation mapping data of the
following document:

Document file: array_pop.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class pop interface':
    '',

    'This page explains the `Array` class `pop` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `pop` method interface removes the last value from an array and returns that value.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `pop` method accepts no arguments and returns the last value, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3])\nlast_value: int = arr.pop()\nassert last_value == 3\n```':  # noqa
    '',

    '':
    '',

    '## pop API':
    '',

    '<!-- Docstring: apysc._type.array.Array.pop -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `pop(self) -> ~T`<hr>\n\n**[Interface summary]** Remove this array\'s last value and return it.<hr>\n\n**[Returns]**\n\n- `value`: *\n  - Removed value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> popped_val: int = arr.pop()\n>>> popped_val\n3\n\n>>> arr\nArray([1, 2])\n```':  # noqa
    '',

}
