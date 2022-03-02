"""This module is for the translation mapping data of the
following document:

Document file: assert_equal_and_not_equal.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# assert_equal and assert_not_equal interfaces':
    '',

    'This page explains the `assert_equal` and `assert_not_equal` function interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `assert_equal` function interface asserts that two JavaScript values are equal. The `assert_not_equal` function interface asserts that the two JavaScript values are not equal.':  # noqa
    '',

    '## See also':
    '',

    '- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)':  # noqa
    '',

    '## Basic usage':
    '',

    'The `assert_equal` and `assert_not_equal` interfaces requires the `left` and `right` arguments. The `msg` argument is optional.\n\nIf the `left` value and `right` values are not the same, the `assert_equal` assertion fails and display an error message on the browser console:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=11, right=int_1, msg=\'Values are not equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_equal_basic_usage/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_equal]\nLeft-side variable name: i_11\nLeft value: 11 right value: 10\n...\nAssertion failed: Values are not equal!\n```':  # noqa
    '',

    '<iframe src="static/assert_equal_basic_usage/index.html" width="0" height="0"></iframe>\n\nThe `assert_not_equal` interface has the same arguments, and if the `left` value and `right` value are the same values, an assertion fails:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_1: ap.Int = ap.Int(10)\nap.assert_not_equal(left=10, right=int_1, msg=\'Values are equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_not_equal_basic_usage/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_not_equal]\nRight-side variable name: i_11\nLeft value: 10 right value: 10\n...\nAssertion failed: Values are equal!\n```':  # noqa
    '',

    '<iframe src="static/assert_not_equal_basic_usage/index.html" width="0" height="0"></iframe>':  # noqa
    '',

    '## assert_equal API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_equal -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_equal(left:Any, right:Any, *, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for equal condition.<hr>\n\n**[Parameters]**\n\n- `left`: *\n  - Left-side value to compare.\n- `right`: *\n  - Right-side value to compare.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Notes]**\n\n ・If specified values are types of Array (or list), then this interface calls the assert_arrays_equal function instead. <br> ・If specified values are types of Dictionary (or dict), then this interface calls the assert_dicts_equal instead.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_1: ap.Int = ap.Int(10)\n>>> int_2: ap.Int = ap.Int(10)\n>>> ap.assert_equal(int_1, int_2)\n```':  # noqa
    '',

    '':
    '',

    '## assert_not_equal API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_not_equal -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_not_equal(left:Any, right:Any, *, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for not equal condition.<hr>\n\n**[Parameters]**\n\n- `left`: *\n  - Left-side value to compare.\n- `right`: *\n  - Right-side value to compare.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Notes]**\n\n ・If specified values are types of Array (or list), then this interface calls the assert_arrays_not_equal function instead. <br> ・If specified values are types of Dictionary (or dict), this interface calls the assert_dicts_not_equal function instead.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_1: ap.Int = ap.Int(10)\n>>> int_2: ap.Int = ap.Int(11)\n>>> ap.assert_not_equal(int_1, int_2)\n```':  # noqa
    '',

}
