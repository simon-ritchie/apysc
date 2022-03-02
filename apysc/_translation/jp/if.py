"""This module is for the translation mapping data of the
following document:

Document file: if.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# If':
    '',

    'This page explains the `If` class.\n\nBefore reading on, maybe it is helpful to read the following page (the apysc uses the `If` class for the same reason of each apysc data type):\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## What is the If class?':
    '',

    'The `If` class is the apysc branch instruction class. It behaves like the Python built-in `if` keyword.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `If` class requires the `with` statement, as follows:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\ncondition: ap.Boolean = ap.Boolean(True)\nwith ap.If(condition):\n    ...\n```':  # noqa
    '',

    'The `If` class requires passing the `Boolean` value as the condition.':
    '',

    '## See also':
    '',

    '- [Elif class](elif.md)\n- [Else class](else.md)\n- [Each branch instruction class\'s scope variables reverting setting](branch_instruction_variables_reverting_setting.md)':  # noqa
    '',

    '## If constructor API':
    '',

    '<!-- Docstring: apysc._branch._if.If.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, condition:Union[apysc._type.boolean.Boolean, NoneType], *, locals_:Union[Dict[str, Any], NoneType]=None, globals_:Union[Dict[str, Any], NoneType]=None) -> None`<hr>\n\n**[Interface summary]** A class to append if branch instruction expression.<hr>\n\n**[Parameters]**\n\n- `condition`: Boolean or None\n  - Boolean value to be used for judgment.\n- `locals_`: dict or None, default None\n  - Current scope\'s local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameInterface variables (like Int, Sprite) at the end of an `If` scope. This setting is useful when you don\'t want to update each variable by implementing the `If` scope.\n- `globals_`: dict or None, default None\n  - Current scope\'s global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> condition: ap.Boolean = int_val >= 10\n>>> with ap.If(condition):\n...     ap.trace(\'Int value is greater than equal 10!\')\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Each branch instruction class\'s scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)':  # noqa
    '',

}
