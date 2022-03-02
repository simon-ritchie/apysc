"""This module is for the translation mapping data of the
following document:

Document file: array_join.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class join interface':
    '',

    'This page explains the `Array` class `join` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `join` method returns a joined `String` with the specified separator string.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `join` method requires the `sep` argument as the separator, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2, 3])\njoined: ap.String = arr.join(sep=\',\')\nassert joined == \'1,2,3\'\n```':  # noqa
    '',

    '':
    '',

    '## join API':
    '',

    '<!-- Docstring: apysc._type.array.Array.join -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `join(self, sep:Union[str, apysc._type.string.String]) -> apysc._type.string.String`<hr>\n\n**[Interface summary]** Join this array value with a specified separator string.<hr>\n\n**[Parameters]**\n\n- `sep`: String or str\n  - Separator string.\n\n<hr>\n\n**[Returns]**\n\n- `joined`: String\n  - Joined string.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.join(sep=\', \')\nString(\'1, 2, 3\')\n```':  # noqa
    '',

}
