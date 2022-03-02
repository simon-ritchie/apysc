"""This module is for the translation mapping data of the
following document:

Document file: array_comparison.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class comparison interfaces':
    '',

    'This page explains the `Array` class comparison interfaces (equal and not equal comparison).':  # noqa
    '',

    '## Basic usage':
    '',

    'The `Array` value can compare with a Python built-in `list` value and `Array` value. A return value becomes the `Boolean` type.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 3, 5])\nresult: ap.Boolean = arr == [1, 3, 5]\nassert result\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 3, 5])\nother_arr: ap.Array[int] = ap.Array([1, 3, 5])\nresult: ap.Boolean = arr == other_arr\nassert result\n```':  # noqa
    '',

    'The equal comparison operator (`==`) and not equal comparison operator (`!=`) are supported:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 3, 5])\nresult: ap.Boolean = arr != [2, 4, 6]\nassert result\n```':  # noqa
    '',

}
