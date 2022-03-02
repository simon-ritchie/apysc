"""This module is for the translation mapping data of the
following document:

Document file: assert_defined_and_undefined.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# assert_defined and assert_undefined interfaces':
    '',

    'This page explains the `assert_defined` and `assert_undefined` function interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `assert_defined` function interface asserts specified value is defined (initialized). Conversely, the `assert_undefined` function interface asserts specified value is undefined (not initialized or deleted).':  # noqa
    '',

    '## See also':
    '',

    '- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)':  # noqa
    '',

    '## Basic usage':
    '',

    'Both of the `assert_defined` and `assert_undefined` interfaces requires `value` argument and `msg` argument is optional.\n\nThe following assertion example (`assert_defined` and initialized value) passes:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_val: ap.Int = ap.Int(10)\nap.assert_defined(\n    value=int_val, msg=\'Value is not defined!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_defined_basic_usage_1/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_defined]\nRight-side variable name: i_11\nLeft value: other than undefined right value: 10\n```':  # noqa
    '',

    '<iframe src="static/assert_defined_basic_usage_1/index.html" width="0" height="0"></iframe>\n\nThe following assertion example (`assert_defined` and the deleted value) fails:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_val: ap.Int = ap.Int(10)\nap.append_js_expression(\n    expression=f\'{int_val.variable_name} = undefined;\')\nap.assert_defined(\n    value=int_val, msg=\'Value is not defined!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_defined_basic_usage_2/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_defined]\nRight-side variable name: i_11\nLeft value: other than undefined right value: undefined\n...\nAssertion failed: Value is not defined!\n```':  # noqa
    '',

    '<iframe src="static/assert_defined_basic_usage_2/index.html" width="0" height="0"></iframe>\n\nThe following assertion example (`assert_undefined` and the deleted value) passes:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_val: ap.Int = ap.Int(10)\nap.append_js_expression(\n    expression=f\'{int_val.variable_name} = undefined;\')\nap.assert_undefined(\n    value=int_val, msg=\'Value is defined!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_undefined_basic_usage_1/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_undefined]\nRight-side variable name: i_11\nLeft value: undefined right value: undefined\n```':  # noqa
    '',

    '<iframe src="static/assert_undefined_basic_usage_1/index.html" width="0" height="0"></iframe>':  # noqa
    '',

    '## assert_defined API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_defined -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_defined(value:Any, *, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for defined (not undefined) value condition.<hr>\n\n**[Parameters]**\n\n- `value`: *\n  - Target value to check.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.assert_defined(int_val)\n```':  # noqa
    '',

    '':
    '',

    '## assert_undefined API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_undefined -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_undefined(value:Any, *, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for undefined value condition.<hr>\n\n**[Parameters]**\n\n- `value`: *\n  - Target value to check.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.append_js_expression(\n...     expression=f\'{int_val.variable_name} = undefined;\')\n>>> ap.assert_undefined(int_val)\n```':  # noqa
    '',

}
