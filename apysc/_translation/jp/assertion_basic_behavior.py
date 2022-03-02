"""This module is for the translation mapping data of the
following document:

Document file: assertion_basic_behavior.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# JavaScript assertion interface basic behaviors':
    '',

    'This page explains the JavaScript assertion interface basic behavior.':
    '',

    '## Interface names':
    '',

    'Each JavaScript assertion interface has the prefix of the `assert_` (e.g., `assert_equal`, `assert_true`, and so on).\n\nThese interfaces are positioned in the root package so you can use them, for example, `ap.assert_equal(...)`.':  # noqa
    '',

    '## Assertion results':
    '',

    'These interfaces display the results on the browser console, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=10, right=int_1)\nap.save_overall_html(\n    dest_dir_path=\'assertion_basic_behavior_results/\')\n```':  # noqa
    '',

    'This code displays the information message on the browser console, like this (please press the F12 key to see):':  # noqa
    '',

    '```\n[assert_equal]\nRight-side variable name: i_11\nLeft value: 10 right value: 10\n```':  # noqa
    '',

    '<iframe src="static/assertion_basic_behavior_results/index.html" width="0" height="0"></iframe>\n\nIf the assertion fails, then an error message also is displayed on the browser console:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=11, right=int_1)\nap.save_overall_html(\n    dest_dir_path=\'assertion_basic_behavior_results_failed/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_equal]\nRight-side variable name: i_11\nLeft value: 11 right value: 10\n...\nAssertion failed:\n...\n```':  # noqa
    '',

    '<iframe src="static/assertion_basic_behavior_results_failed/index.html" width="0" height="0"></iframe>':  # noqa
    '',

    '## Optional msg argument':
    '',

    'Each assertion interface has the `msg` optional argument. If you provide this argument, the error message is displayed on the browser console when an assertion fails.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nint_1: ap.Int = ap.Int(10)\nap.assert_equal(left=11, right=int_1, msg=\'Values are not equal!\')\nap.save_overall_html(\n    dest_dir_path=\'assertion_basic_behavior_msg/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_equal]\nRight-side variable name: i_11\nLeft value: 11 right value: 10\n...\nAssertion failed: Values are not equal!\n```':  # noqa
    '',

    '<iframe src="static/assertion_basic_behavior_msg/index.html" width="0" height="0"></iframe>':  # noqa
    '',

}
