"""This module is for the translation mapping data of the
following document:

Document file: math_clamp.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Math clamp interface": "# Math クラスの clamp インターフェイス",
    ##################################################
    "This page explains the `Math` class's `clamp` class method interface.": "このページでは`Math`クラスの`clamp`メソッドについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `clamp` method sets the value within a specified minimum and maximum range.": "`clamp`メソッドは指定された最小値と最大値の範囲内で値を設定します。",  # noqa
    ##################################################
    "For example, if the value is `20` and the minimum is `25`, the result value becomes `25`.": "例えば、もし値が`20`で最小値が`25`の場合、結果の値は`25`になります。",  # noqa
    ##################################################
    "Similarly, if the value is `20` and the maximum is `15`, the result value becomes `15`.": "同様に、もし値が`20`で最大値が`15`であれば、結果の値は`15`になります。",  # noqa
    ##################################################
    "If the value is `20` and the minimum and maximum are `15` and `25`, this method returns the `20` value as is.": "もし値が`20`で最小値と最大値が`15`と`25`であれば、このメソッドはそのまま`20`の値を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `clamp` method requires the `value`, `min_`, and `max_` arguments.": "`clamp`メソッドは`value`、`min_`、`max_`の引数を必要とします。",  # noqa
    ##################################################
    "Each argument and return value becomes the `ap.Int` or `ap.Number` type.": "各引数と返却値は`ap.Int`もしくは`ap.Number`型となります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=1,\n    stage_height=1,\n    stage_elem_id="stage",\n)\nvalue: ap.Int = ap.Int(20)\nresult: ap.Int = ap.Math.clamp(value=value, min_=ap.Int(25), max_=ap.Int(50))\nap.assert_equal(result, ap.Int(25))\n\nresult = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(15))\nap.assert_equal(result, ap.Int(15))\n\nresult = ap.Math.clamp(value=value, min_=ap.Int(15), max_=ap.Int(25))\nap.assert_equal(result, ap.Int(20))\n\nap.save_overall_html(dest_dir_path="math_clamp_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=1,\n    stage_height=1,\n    stage_elem_id="stage",\n)\nvalue: ap.Int = ap.Int(20)\nresult: ap.Int = ap.Math.clamp(value=value, min_=ap.Int(25), max_=ap.Int(50))\nap.assert_equal(result, ap.Int(25))\n\nresult = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(15))\nap.assert_equal(result, ap.Int(15))\n\nresult = ap.Math.clamp(value=value, min_=ap.Int(15), max_=ap.Int(25))\nap.assert_equal(result, ap.Int(20))\n\nap.save_overall_html(dest_dir_path="math_clamp_basic_usage/")\n```',  # noqa
    ##################################################
    "## clamp method API": "## clamp メソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Sets the value within a specified minimum and maximum range. If the value is less than the minimum, this method returns the minimum value. If the value is greater than the maximum, this method returns the maximum value.<hr>": "指定された最小値と最大値の範囲内で値を設定します。もし値が最小値未満であればこのメソッドは最小値を返却します。もし値が最大値よりも大きければこのメソッドは最大値を返却します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: _ValueType": "- `value`: _ValueType",
    ##################################################
    "  - Target `Int` or `Number` value.": "  - 対象の`Int`もしくは`Number`型の値。",
    ##################################################
    "- `min_`: _ValueType": "- `min_`: _ValueType",
    ##################################################
    "  - Minimum value.": "  - 最小値。",
    ##################################################
    "- `max_`: _ValueType": "- `max_`: _ValueType",
    ##################################################
    "  - Maximum value.": "  - 最大値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result`: _ValueType": "- `result`: _ValueType",
    ##################################################
    "  - Clamped value.": "  - 最小値と最大値範囲の反映後の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> value: ap.Int = ap.Int(5)\n>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))\n>>> value\nInt(10)\n\n>>> value = ap.Int(25)\n>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))\n>>> value\nInt(20)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> value: ap.Int = ap.Int(5)\n>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))\n>>> value\nInt(10)\n\n>>> value = ap.Int(25)\n>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))\n>>> value\nInt(20)\n```",  # noqa
}
