"""This module is for the translation mapping data of the
following document:

Document file: assert_defined_and_undefined.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# assert_defined and assert_undefined interfaces':
    '# assert_defined と assert_undefined のインターフェイス',

    'This page explains the `assert_defined` and `assert_undefined` function interfaces.':  # noqa
    'このページでは`assert_defined`と`assert_undefined`の関数の各インターフェイスについて説明します。',

    '## What interfaces are these?':
    '## 各インターフェイスの概要',

    'The `assert_defined` function interface asserts specified value is defined (initialized). Conversely, the `assert_undefined` function interface asserts specified value is undefined (not initialized or deleted).':  # noqa
    '`assert_defined`関数のインターフェイスは指定された値が定義済みかどうか（初期化されているか）をチェックします。逆に`assert_undefined`関数は指定された値が定義されていない（`undefine`）状態や削除済みかどうかなどをチェックします。',  # noqa

    '## See also':
    '## 関連資料',

    '- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)':  # noqa
    '- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)',  # noqa

    '## Basic usage':
    '## 基本的な使い方',

    'Both of the `assert_defined` and `assert_undefined` interfaces requires `value` argument and `msg` argument is optional.':  # noqa
    '`assert_defined`と`assert_undefined`の各インターフェイスは共に`value`引数が必要になります。`msg`引数は省略可です。',  # noqa

    'The following assertion example (`assert_defined` and initialized value) passes:':  # noqa
    '以下のコード例では初期化されている値に対して`assert_defined`関数でチェックを行っています（チェックを通ります）:',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_val: ap.Int = ap.Int(10)\nap.assert_defined(\n    value=int_val, msg=\'Value is not defined!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_defined_basic_usage_1/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_val: ap.Int = ap.Int(10)\nap.assert_defined(\n    value=int_val, msg=\'Value is not defined!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_defined_basic_usage_1/\')\n```',  # noqa

    '```\n[assert_defined]\nRight-side variable name: i_11\nLeft value: other than undefined right value: 10\n```':  # noqa
    '```\n[assert_defined]\nRight-side variable name: i_11\nLeft value: other than undefined right value: 10\n```',  # noqa

    'The following assertion example (`assert_defined` and the deleted value) fails:':  # noqa
    '以下のコード例では削除の済みの値に対して`assert_defined`関数でチェックをしています（チェックは失敗します）:',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_val: ap.Int = ap.Int(10)\nap.append_js_expression(\n    expression=f\'{int_val.variable_name} = undefined;\')\nap.assert_defined(\n    value=int_val, msg=\'Value is not defined!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_defined_basic_usage_2/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_val: ap.Int = ap.Int(10)\nap.append_js_expression(\n    expression=f\'{int_val.variable_name} = undefined;\')\nap.assert_defined(\n    value=int_val, msg=\'Value is not defined!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_defined_basic_usage_2/\')\n```',  # noqa

    '```\n[assert_defined]\nRight-side variable name: i_11\nLeft value: other than undefined right value: undefined\n...\nAssertion failed: Value is not defined!\n```':  # noqa
    '```\n[assert_defined]\nRight-side variable name: i_11\nLeft value: other than undefined right value: undefined\n...\nAssertion failed: Value is not defined!\n```',  # noqa

    'The following assertion example (`assert_undefined` and the deleted value) passes:':  # noqa
    '以下のコード例では削除済みの値に対して`assert_undefined`関数でチェックを行っています（チェックは通ります）:',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_val: ap.Int = ap.Int(10)\nap.append_js_expression(\n    expression=f\'{int_val.variable_name} = undefined;\')\nap.assert_undefined(\n    value=int_val, msg=\'Value is defined!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_undefined_basic_usage_1/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_val: ap.Int = ap.Int(10)\nap.append_js_expression(\n    expression=f\'{int_val.variable_name} = undefined;\')\nap.assert_undefined(\n    value=int_val, msg=\'Value is defined!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_undefined_basic_usage_1/\')\n```',  # noqa

    '```\n[assert_undefined]\nRight-side variable name: i_11\nLeft value: undefined right value: undefined\n```':  # noqa
    '```\n[assert_undefined]\nRight-side variable name: i_11\nLeft value: undefined right value: undefined\n```',  # noqa

    '## assert_defined API':
    '## assert_defined API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** JavaScript assertion interface for defined (not undefined) value condition.<hr>':  # noqa
    '**[Interface summary]** JavaScriptでの値が定義済みかどうかのチェックを行うインターフェイスです。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `value`: *':
    '- `value`: *',

    '  - Target value to check.':
    '  - チェック対象の値。',

    '- `msg`: str, optional':
    '- `msg`: str, optional',

    '  - Message to display when assertion failed.':
    '  - チェックに失敗した際に表示するメッセージ。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.assert_defined(int_val)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.assert_defined(int_val)\n```',  # noqa

    '## assert_undefined API':
    '## assert_undefined API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** JavaScript assertion interface for undefined value condition.<hr>':  # noqa
    '**[インターフェイス概要]** JavaScriptでの値が未定義かどうかのチェックを行うインターフェイスです。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `value`: *':
    '- `value`: *',

    '  - Target value to check.':
    '  - チェック対象の値。',

    '- `msg`: str, optional':
    '- `msg`: str, optional',

    '  - Message to display when assertion failed.':
    '  - チェックに失敗した際に表示するメッセージ。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.append_js_expression(\n...     expression=f\'{int_val.variable_name} = undefined;\')\n>>> ap.assert_undefined(int_val)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.append_js_expression(\n...     expression=f\'{int_val.variable_name} = undefined;\')\n>>> ap.assert_undefined(int_val)\n```',  # noqa

}
