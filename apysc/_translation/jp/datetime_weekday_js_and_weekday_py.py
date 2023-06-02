"""This module is for the translation mapping data of the
following document:

Document file: datetime_weekday_js_and_weekday_py.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class weekday_js and weekday_py properties": "# DateTime クラスの weekday_js と weekday_py 属性",  # noqa
    ##################################################
    "This page explains the `DateTime` class's `weekday_js` and `weekday_py` properties interfaces.": "このページでは`DateTime`クラスの`weekday_js`と`weekday_py`属性の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface are these?": "## 各インターフェイス概要",
    ##################################################
    "The `weekday_js` property gets a JavaScript weekday value (Sunday is 0, and Saturday is 6).": "`weekday_js`属性はJavaScriptの曜日の値（日曜が0となり、土曜が6となります）を取得します。",  # noqa
    ##################################################
    "Similarly, the `weekday_py` property gets a Python weekday value (Monday is 0, and Sunday is 6).": "似たような形で、`weekday_py`属性はPythonの曜日の値（月曜が0となり、日曜が6となります）を取得します。",  # noqa
    ##################################################
    "These interfaces have only the getter interface (there is no setter interface).": "これらのインターフェイスはgetterのインターフェイスのみ存在します（setterのインターフェイスは存在しません）。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "A `DateTime` instance has these properties interfaces.": "`DateTime`クラスのインスタンスがこれらの各属性のインターフェイスを持っています。",  # noqa
    ##################################################
    "These getter interfaces return a weekday's `Int` value.": "これらのgetterのインターフェイスは`Int`型の曜日の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\n# 2022-12-11 is Sunday.\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=11)\nweekday_js: ap.Int = datetime_.weekday_js\nassert weekday_js == 0\n\nweekday_py: ap.Int = datetime_.weekday_py\nassert weekday_py == 6\n```": "```py\n# runnable\nimport apysc as ap\n\n# 2022-12-11 is Sunday.\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=11)\nweekday_js: ap.Int = datetime_.weekday_js\nassert weekday_js == 0\n\nweekday_py: ap.Int = datetime_.weekday_py\nassert weekday_py == 6\n```",  # noqa
    ##################################################
    "## weekday_js property API": "## weekday_js 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current weekday value. This interface sets the weekday based on the JavaScript value as follows: ": "現在の曜日の値を取得します。このインターフェイスは以下のようにJavaScriptの曜日の値をベースとした値を設定します。",  # noqa
    ##################################################
    "<br> ・0 -> Sunday ": "<br> ・0 -> 日曜 ",
    ##################################################
    "<br> ・1 -> Monday ": "<br> ・1 -> 月曜 ",
    ##################################################
    "<br> ・2 -> Tuesday ": "<br> ・2 -> 火曜 ",
    ##################################################
    "<br> ・3 -> Wednesday ": "<br> ・3 -> 水曜 ",
    ##################################################
    "<br> ・4 -> Thursday ": "<br> ・4 -> 木曜 ",
    ##################################################
    "<br> ・5 -> Friday ": "<br> ・5 -> 金曜 ",
    ##################################################
    "<br> ・6 -> Saturday<hr>": "<br> ・6 -> 土曜<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `weekday`: Int": "- `weekday`: Int",
    ##################################################
    "  - A current weekday value.": "  - 現在の曜日の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=4)\n>>> datetime_.weekday_js  # Sunday\nInt(0)\n\n>>> datetime_ = ap.DateTime(year=2022, month=12, day=10)\n>>> datetime_.weekday_js  # Saturday\nInt(6)\n```": "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=4)\n>>> datetime_.weekday_js  # Sunday\nInt(0)\n\n>>> datetime_ = ap.DateTime(year=2022, month=12, day=10)\n>>> datetime_.weekday_js  # Saturday\nInt(6)\n```",  # noqa
    ##################################################
    "## weekday_py property API": "## weekday_py 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current weekday value. This interface sets the weekday based on the Python value as follows: ": "現在の曜日の値を取得します。このインターフェイスは以下のようにPythonの曜日の値をベースとした値を設定します。",  # noqa
    ##################################################
    "<br> ・0 -> Monday ": "<br> ・0 -> 月曜 ",
    ##################################################
    "<br> ・1 -> Thursday ": "<br> ・1 -> 火曜 ",
    ##################################################
    "<br> ・2 -> Wednesday ": "<br> ・2 -> 水曜 ",
    ##################################################
    "<br> ・3 -> Thursday ": "<br> ・3 -> 木曜 ",
    ##################################################
    "<br> ・4 -> Friday ": "<br> ・4 -> 金曜 ",
    ##################################################
    "<br> ・5 -> Saturday ": "<br> ・5 -> 土曜 ",
    ##################################################
    "<br> ・6 -> Sunday<hr>": "<br> ・6 -> 日曜<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `weekday`: Int": "- `weekday`: Int",
    ##################################################
    "  - A current weekday value.": "  - 現在の曜日の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\n>>> datetime_.weekday_py  # Monday\nInt(0)\n\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=4)\n>>> datetime_.weekday_py  # Sunday\nInt(6)\n```": "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\n>>> datetime_.weekday_py  # Monday\nInt(0)\n\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=4)\n>>> datetime_.weekday_py  # Sunday\nInt(6)\n```",  # noqa
}
