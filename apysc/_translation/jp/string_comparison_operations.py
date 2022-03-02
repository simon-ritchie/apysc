"""This module is for the translation mapping data of the
following document:

Document file: string_comparison_operations.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# String class comparison operations':
    '',

    'This page explains the `String` class comparison operations, like the `=`\\, `>=`\\.':  # noqa
    '',

    '## Comparison return value type':
    '',

    'Each `String` class comparison operation returns a `Boolean` value, not a Python built-in `bool` value.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nresult: ap.Boolean = string_1 == \'Hello\'\nassert result\nassert isinstance(result, ap.Boolean)\n```':  # noqa
    '',

    '':
    '',

    '## Acceptable comparison right-side value types':
    '',

    'The `str` or `String` types of comparison other value (comparison right-side value) types are acceptable, for instance:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nresult: ap.Boolean = string_1 == \'Hello\'\nassert result\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nstring_2: ap.String = ap.String(\'Hello\')\nresult: ap.Boolean = string_1 == string_2\nassert result\n```':  # noqa
    '',

    '':
    '',

    '## Equal comparison':
    '',

    'You can use the `==` operator for the equal comparison:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nresult: ap.Boolean = string_1 == \'Hello\'\nassert result\n```':  # noqa
    '',

    '':
    '',

    '## Not equal comparison':
    '',

    'You can use the `!=` operator for the not equal comparison:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nresult: ap.Boolean = string_1 != \'World\'\nassert result\n```':  # noqa
    '',

    '':
    '',

    '## Less than or greater than comparison':
    '',

    'You can use each less than, less than or equal, greater than, greater than equal comparison, with the `<`\\, `<=`\\, `>`\\, `>=` operators, like the Python built-in `str` value. Sometimes these operations are helpful to compare with the date (or date-time) string.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'1970-01-05\')\nresult: ap.Boolean = string_1 < \'1970-01-06\'\nassert result\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'1970-01-05\')\nresult: ap.Boolean = string_1 <= \'1970-01-05\'\nassert result\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'1970-01-05\')\nresult: ap.Boolean = string_1 > \'1970-01-04\'\nassert result\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'1970-01-05\')\nresult: ap.Boolean = string_1 >= \'1970-01-05\'\nassert result\n```':  # noqa
    '',

}
