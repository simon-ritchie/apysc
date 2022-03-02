"""This module is for the translation mapping data of the
following document:

Document file: array_insert_and_insert_at.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class insert and insert_at interfaces':
    '',

    'This page explains the `Array` class `insert` and `insert_at` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `insert` and `insert_at` method interfaces append any value at the specified index. Both interfaces behave the same way (the `insert` is the alias of the `insert_at`).':  # noqa
    '',

    '## Basic usage':
    '',

    'The `insert` and `insert_at` have the same argument, the `index` and `value`\\. The `index` argument accepts an `int` and `Int` value.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 4])\narr.insert(index=1, value=2)\nassert arr == [1, 2, 4]\n\nindex: ap.Int = ap.Int(2)\narr.insert_at(index=index, value=3)\nassert arr == [1, 2, 3, 4]\n```':  # noqa
    '',

    '':
    '',

    '## insert API':
    '',

    '<!-- Docstring: apysc._type.array.Array.insert -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `insert(self, index:Union[int, apysc._type.int.Int], value:~T) -> None`<hr>\n\n**[Interface summary]** Insert value to this array at a specified index. This interface behaves the same `insert_at` method.<hr>\n\n**[Parameters]**\n\n- `index`: Int or int\n  - Index to append value.\n- `value`: *\n  - Any value to append.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 3])\n>>> arr.insert(index=1, value=2)\n>>> arr\nArray([1, 2, 3])\n```':  # noqa
    '',

    '':
    '',

    '## insert_at API':
    '',

    '<!-- Docstring: apysc._type.array.Array.insert_at -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `insert_at(self, index:Union[int, apysc._type.int.Int], value:~T) -> None`<hr>\n\n**[Interface summary]** Insert value to this array at a specified index. This interface behaves the same `insert` method.<hr>\n\n**[Parameters]**\n\n- `index`: Int or int\n  - Index to append value.\n- `value`: *\n  - Any value to append.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 3])\n>>> arr.insert_at(index=1, value=2)\n>>> arr\nArray([1, 2, 3])\n```':  # noqa
    '',

}
