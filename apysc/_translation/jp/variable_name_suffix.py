"""This module is for the translation mapping data of the
following document:

Document file: variable_name_suffix.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# variable_name_suffix argument setting": "# variable_name_suffix の引数設定",
    ##################################################
    "This page explains the `variable_name_suffix` argument setting.": "このページでは`variable_name_suffix`の引数設定について説明します。",  # noqa
    ##################################################
    "## What argument is this?": "## 引数の概要",
    ##################################################
    "The `variable_name_suffix` argument changes an exported JavaScript's variable name suffix.": "`variable_name_suffix`引数は出力されるJavaScriptの変数名のサフィックスを変更します。",  # noqa
    ##################################################
    "This setting sometimes becomes useful when you want to debug an exported JavaScript code.": "この設定は出力されたJavaScriptに対してデバッグを行う際などに便利なことがあります。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Each class has a `variable_name_suffix`, and you can set a suffix with its argument.": "apyscの各クラスは`variable_name_suffix`引数を持っており、その引数を使ってサフィックスを設定することができます。",  # noqa
    ##################################################
    "The following example sets the `my_int` suffix to the `ap.Int` instance:": "以下のコード例では`my_int`というサフィックスを`ap.Int`クラスのインスタンスへと設定しています:",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nap.Stage(stage_width=150, stage_height=150, stage_elem_id="stage")\nint_val: ap.Int = ap.Int(10, variable_name_suffix="my_int")\nap.trace(int_val)\n\nap.save_overall_html(\n    dest_dir_path="./variable_name_suffix_basic_usage_1/", minify=False\n)\n```': '```py\nimport apysc as ap\n\nap.Stage(stage_width=150, stage_height=150, stage_elem_id="stage")\nint_val: ap.Int = ap.Int(10, variable_name_suffix="my_int")\nap.trace(int_val)\n\nap.save_overall_html(\n    dest_dir_path="./variable_name_suffix_basic_usage_1/", minify=False\n)\n```',  # noqa
    ##################################################
    "In the exported JavaScript code, you can verify its `ap.Int` variable has the specified suffix, `_my_int`, as follows:": "出力されたJavaScriptコード内で、`ap.Int`クラスが変換されて作成された変数が以下のように指定された`_my_int`というサフィックスを持っていることを確認できます:",  # noqa
    ##################################################
    '```js\n  // ...\n  var i_9__my_int = 10;\n  console.log(i_9__my_int, "Called from: tmp.py, line number: 5");\n  // ...\n```': '```js\n  // ...\n  var i_9__my_int = 10;\n  console.log(i_9__my_int, "Called from: tmp.py, line number: 5");\n  // ...\n```',  # noqa
    ##################################################
    "Class attributes inherit a suffix value of its class argument's value.": "クラスの属性の値はそのクラスへ指定されたサフィックスの値を引き継ぎます。",  # noqa
    ##################################################
    "For example, if you set the `my_rectangle` value to the `variable_name_suffix` argument, its attributes (e.g., `x`, `fill_color`) also inherit the `my_rectangle` suffix:": "例えば`variable_name_suffix`引数に`my_rectangle`というサフィックスを指定した場合、そのクラスの属性（例 : `x`や`fill_color`など）は同様に`my_rectangle`というサフィックスを持つようになります:",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nap.Stage(stage_width=150, stage_height=150, stage_elem_id="stage")\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Color("#0af"),\n    variable_name_suffix="my_rectangle",\n)\n\nap.save_overall_html(\n    dest_dir_path="./variable_name_suffix_basic_usage_2/", minify=False\n)\n```': '```py\nimport apysc as ap\n\nap.Stage(stage_width=150, stage_height=150, stage_elem_id="stage")\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Color("#0af"),\n    variable_name_suffix="my_rectangle",\n)\n\nap.save_overall_html(\n    dest_dir_path="./variable_name_suffix_basic_usage_2/", minify=False\n)\n```',  # noqa
    ##################################################
    "In that case, each attribute also has an attribute identifier suffix, such as the `x`, `width`:": "このようなケースでは`x`や`width`などの属性の識別用のサフィックスも同様に設定されます:",  # noqa
    ##################################################
    '```js\n  var i_9__my_rectangle__x = 50;\n  var i_10__my_rectangle__y = 50;\n  var i_12__my_rectangle__width = 50;\n  // ...\n  var rect_1__my_rectangle = stage\n    .rect(i_16__my_rectangle__width, i_17__my_rectangle__height)\n    .attr({\n      fill: s_1__my_rectangle__fill_color,\n      "fill-opacity": n_2__my_rectangle__fill_alpha,\n      "stroke-width": i_15__my_rectangle__line_thickness,\n      "stroke-opacity": n_3__my_rectangle__line_alpha,\n      x: i_9__my_rectangle__x,\n      y: i_10__my_rectangle__y,\n    });\n  // ...\n```': '```js\n  var i_9__my_rectangle__x = 50;\n  var i_10__my_rectangle__y = 50;\n  var i_12__my_rectangle__width = 50;\n  // ...\n  var rect_1__my_rectangle = stage\n    .rect(i_16__my_rectangle__width, i_17__my_rectangle__height)\n    .attr({\n      fill: s_1__my_rectangle__fill_color,\n      "fill-opacity": n_2__my_rectangle__fill_alpha,\n      "stroke-width": i_15__my_rectangle__line_thickness,\n      "stroke-opacity": n_3__my_rectangle__line_alpha,\n      x: i_9__my_rectangle__x,\n      y: i_10__my_rectangle__y,\n    });\n  // ...\n```',  # noqa
}
