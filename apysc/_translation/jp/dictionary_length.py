"""This module is for the translation mapping data of the
following document:

Document file: dictionary_length.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Dictionary length interface':
    '',

    'This page explains the `Dictionary` class `length` property interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `length` property returns the length of dictionary keys.':
    '',

    '## Basic usage':
    '',

    'The `length` property interface returns the `Int` value. There is no setter interface.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({\'a\': 10, \'b\': 20})\nassert dict_1.length == 2\nassert isinstance(dict_1.length, ap.Int)\n```':  # noqa
    '',

    '':
    '',

    '## Note for the len function':
    '',

    'The Python built-in `len` function is not supported and raises an exception:':  # noqa
    '',

    '```py\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({\'a\': 10, \'b\': 20})\nlen(dict_1)\n```':  # noqa
    '',

    '':
    '',

    '```\nException: Dictionary instance can\'t apply len function. Please use length property instead.\n```':  # noqa
    '',

    '':
    '',

    '## length property API':
    '',

    '<!-- Docstring: apysc._type.dictionary.Dictionary.length -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get length of this dictionary values.<hr>\n\n**[Returns]**\n\n- `length`: Int\n  - This dictionary value\'s length.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({\'a\': 1, \'b\': 2})\n>>> dictionary.length\nInt(2)\n```':  # noqa
    '',

}
