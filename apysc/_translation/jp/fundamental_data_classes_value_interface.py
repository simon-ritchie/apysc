"""This module is for the translation mapping data of the
following document:

Document file: fundamental_data_classes_value_interface.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# apysc fundamental data classes value interface':
    '',

    'This page explains the apysc fundamental data classes (such as the `Int`\\, `Number`\\, `String`) `value` interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `value` getter interface returns each data class value. And the setter interface updates these data class values.\n\nA return value of the getter interface becomes a Python built-in value, like the `int`\\, `float`\\, `str`\\, `list`\\.':  # noqa
    '',

    '## Basic usage of the getter interface':
    '',

    'The `value` getter interface returns the Python built-in value.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nvalue = int_1.value\nassert isinstance(value, int)\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nvalue = number_1.value\nassert isinstance(value, float)\n```':  # noqa
    '',

    '':
    '',

    '## Basic usage of the setter interface':
    '',

    'You can update the apysc fundamental data class values with the `value` setter interface. Python built-in values and the same type value is acceptable:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_1.value = 20\nassert int_1 == 20\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_1.value = ap.Int(20)\nassert int_1 == 20\n```':  # noqa
    '',

}
