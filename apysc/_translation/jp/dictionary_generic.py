"""This module is for the translation mapping data of the
following document:

Document file: dictionary_generic.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Dictionary class generic type settings':
    '',

    'This page explains the `Dictionary` class key and value\'s generic type settings.':  # noqa
    '',

    '## Basic usage':
    '',

    'You can specify the key and value\'s type at the `Dictionary` type-annotation, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\ndict_value: ap.Dictionary[str, int] = ap.Dictionary({\'a\': 10})\na_value: int = dict_value[\'a\']\n```':  # noqa
    '',

    'These generic type-annotations are sometimes helpful for checking with the mypy, Pylance, or other libraries and enhancing safety.\n\nFor example, the following code raises an error of value\'s type when checking with the Pylance:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\ndict_value: ap.Dictionary[str, int] = ap.Dictionary({\'a\': 10})\na_value: str = dict_value[\'a\']\n```':  # noqa
    '',

    '':
    '',

    '```\nExpression of type "int" cannot be assigned to declared type "str"\n  "int" is incompatible with "str"\n```':  # noqa
    '',

    'Also, the following code raises an error of key\'s type (`str` is required but `int` is specified):':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\ndict_value: ap.Dictionary[str, int] = ap.Dictionary({\'a\': 10})\na_value: int = dict_value[10]\n```':  # noqa
    '',

    'If you need to use multiple types and type checking, then use the `Union`\\, as follows:\n\nNotes: Alternatively, use the `|` symbol, if you are using Python 3.10 or later) or `Any` type.':  # noqa
    '',

    '```py\n# runnable\nfrom typing import Union\n\nimport apysc as ap\n\n# Accepting the str and int key types.\ndict_value: ap.Dictionary[Union[int, str], int] = ap.Dictionary(\n    {\'a\': 10, 2: 20})\na_value: int = dict_value[\'a\']\nb_value: int = dict_value[2]\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nfrom typing import Any\n\nimport apysc as ap\n\n# Accepting all types by specifying the Any type.\ndict_value: ap.Dictionary[Any, Any] = ap.Dictionary(\n    {\'a\': 10, 2: \'b\'})\na_value: int = dict_value[\'a\']\nb_value: str = dict_value[2]\n```':  # noqa
    '',

}
