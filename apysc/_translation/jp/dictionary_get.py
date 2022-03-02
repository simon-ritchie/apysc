"""This module is for the translation mapping data of the
following document:

Document file: dictionary_get.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Dictionary get interface':
    '',

    'This page explains the `Dictionary` class `get` method interface.':
    '',

    '## What interface is this?':
    '',

    'The `get` method returns the specified key\'s value. If that key does not exist in the dictionary, it returns the default value (not raising an exception).':  # noqa
    '',

    '## Basic usage':
    '',

    'The `get` method requires the first argument, `key` (dictionary key). The second argument of the `default` is optional, and if not provided, it returns the `None` value.':  # noqa
    '',

    '```py\n# runnable\nfrom typing import Any, Optional\n\nimport apysc as ap\n\ndict_val: ap.Dictionary = ap.Dictionary({\'a\': 10})\ngot_val_1: int = dict_val.get(key=\'a\', default=0)\nassert got_val_1 == 10\n\ngot_val_2: int = dict_val.get(key=\'b\', default=0)\nassert got_val_2 == 0\n\ngot_val_3: Optional[Any] = dict_val.get(key=\'b\')\nassert got_val_3 is None\n```':  # noqa
    '',

    '':
    '',

    '## get API':
    '',

    '<!-- Docstring: apysc._type.dictionary.Dictionary.get -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `get(self, key:Union[~_K, apysc._type.expression_string.ExpressionString], *, default:~DefaultType=None) -> ~DefaultType`<hr>\n\n**[Interface summary]** Get a specified key dictionary value. If this dictionary hasn\'t a specified key, this interface returns a default value.<hr>\n\n**[Parameters]**\n\n- `key`: _K\n  - Target key.\n- `default`: DefaultType or None, optional\n  - Any default value.\n\n<hr>\n\n**[Returns]**\n\n- `result_value`: Any\n  - Extracted value or a default value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> from typing import Optional\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({\'a\': 10})\n>>> value_1: Optional[int] = dictionary.get(\'a\')\n>>> value_1\n10\n\n>>> value_2: Optional[int] = dictionary.get(\'b\')\n>>> print(value_2)\nNone\n\n>>> value_3: int = dictionary.get(\'c\', default=0)\n>>> value_3\n0\n```':  # noqa
    '',

}
