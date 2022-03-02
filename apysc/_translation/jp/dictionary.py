"""This module is for the translation mapping data of the
following document:

Document file: dictionary.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Dictionary':
    '',

    'This page explains the `Dictionary` class.\n\nBefore reading on, maybe it is helpful to read the following page:\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## What is the Dictionary?':
    '',

    'The `Dictionary` class is the apysc dictionary class. It behaves like the Python built-in `dict` value.':  # noqa
    '',

    '## Constructor method':
    '',

    'The `Dictionary` class constructor method requires a Python built-in `dict` or `Dictionary` value:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({\'a\': 10})\nassert dict_1 == {\'a\': 10}\n\ndict_2: ap.Dictionary = ap.Dictionary(dict_1)\nassert dict_1 == dict_2\n```':  # noqa
    '',

    '':
    '',

    '## Value setter interface':
    '',

    'A `Dictionary` value can be updated by indexing, like the Python built-in `dict` value:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({\'a\': 10})\ndict_1[\'a\'] = 20\nassert dict_1 == {\'a\': 20}\n```':  # noqa
    '',

    '':
    '',

    '## Value getter interface':
    '',

    'A `Dictionary` value also can be retrieved by indexing:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\ndict_1: ap.Dictionary = ap.Dictionary({\'a\': int_1})\nint_2: ap.Int = dict_1[\'a\']\nassert isinstance(int_2, ap.Int)\nassert int_2 == 10\n```':  # noqa
    '',

    '':
    '',

    '## Notes of the getter interface':
    '',

    'If a `Dictionary` value doesn\'t have the specified key, a retrieved value type becomes the `AnyValue` type. This behavior occasionally is helpful when a `Dictionary` value is updated dynamically (e.g., updating by the JavaScript event handler).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\ndict_1: ap.Dictionary = ap.Dictionary({\'a\': int_1})\nretrieved_val: ap.AnyValue = dict_1[\'b\']\nassert isinstance(retrieved_val, ap.AnyValue)\n```':  # noqa
    '',

    '':
    '',

    '## Value deletion interface':
    '',

    'A `Dictionary` value can be deleted by the `del` statement, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\ndict_1: ap.Dictionary = ap.Dictionary({\'a\': int_1})\ndel dict_1[\'a\']\nassert dict_1 == {}\n```':  # noqa
    '',

    '':
    '',

    '## Dictionary class constructor API':
    '',

    '<!-- Docstring: apysc._type.dictionary.Dictionary.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, value:Union[Dict[~_K, ~_V], _ForwardRef(\'Dictionary\')]) -> None`<hr>\n\n**[Interface summary]** Dictionary class for the apysc library.<hr>\n\n**[Parameters]**\n\n- `value`: dict or Dictionary\n  - Initial dictionary value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({\'a\': 10})\n>>> dictionary\nDictionary({\'a\': 10})\n\n>>> dictionary[\'a\']\n10\n\n>>> dictionary[\'b\'] = 20\n>>> dictionary[\'b\']\n20\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Dictionary class generic type settings document](https://simon-ritchie.github.io/apysc/dictionary_generic.html)':  # noqa
    '',

    '## value attribute API':
    '',

    '<!-- Docstring: apysc._type.dictionary.Dictionary.value -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a current dict value.<hr>\n\n**[Returns]**\n\n- `value`: dict\n  - Current dict value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({})\n>>> dictionary.value = {\'a\': 10}\n>>> dictionary.value\n{\'a\': 10}\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)':  # noqa
    '',

}
