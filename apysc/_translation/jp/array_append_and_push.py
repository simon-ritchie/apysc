"""This module is for the translation mapping data of the
following document:

Document file: array_append_and_push.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class append and push interfaces':
    '',

    'This page explains the `Array` class `append` and `push` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `append` and `push` method interfaces append any value to the end of an array. These interfaces behave the same (`append` is similar to the Python built-in and the `push` interface is similar to the JavaScript).':  # noqa
    '',

    '## Basic usage':
    '',

    'The `append` and `push` methods require the first argument of the `value`\\.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2])\narr.append(value=3)\nassert arr == [1, 2, 3]\n\narr.push(value=4)\nassert arr == [1, 2, 3, 4]\n```':  # noqa
    '',

    '':
    '',

    '## append API':
    '',

    '<!-- Docstring: apysc._type.array.Array.append -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `append(self, value:~T) -> None`<hr>\n\n**[Interface summary]** Add any value to the end of this array. This method behaves the same `push` method.<hr>\n\n**[Parameters]**\n\n- `value`: *\n  - Any value to append.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.append(4)\n>>> arr\nArray([1, 2, 3, 4])\n```':  # noqa
    '',

    '':
    '',

    '## push API':
    '',

    '<!-- Docstring: apysc._type.array.Array.push -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `push(self, value:~T) -> None`<hr>\n\n**[Interface summary]** Add any value to the end of this array. This interface behaves the same as the `append` method.<hr>\n\n**[Parameters]**\n\n- `value`: *\n  - Any value to append.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.push(4)\n>>> arr\nArray([1, 2, 3, 4])\n```':  # noqa
    '',

}
