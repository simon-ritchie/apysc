"""This module is for the translation mapping data of the
following document:

Document file: timedelta_total_seconds.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# TimeDelta class total_seconds interface": "# TimeDelta クラスの total_seconds インターフェイス",  # noqa
    ##################################################
    "This page explains the `TimeDelta` class's `total_seconds` method interface.": "このページでは`TimeDelta`クラスの`total_seconds`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `total_seconds` method returns the number of total seconds between two `DateTime` instances.": "`total_seconds`メソッドは2つの`DateTime`クラスのインスタンス間の合計秒数を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `total_seconds` method returns the apysc's `Number` value.": "`total_seconds`メソッドはapyscの`Number`型の値を返却します。",  # noqa
    ##################################################
    "If any `DateTime` instances have a `millisecond` value, this interface sets a fraction value.": "もしもいずれかの`DateTime`のインスタンスが`millisecond`属性の値を持っていた場合このインターフェイスは小数点数も含んだ値を設定します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7, millisecond=100)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\ntotal_seconds: ap.Number = timedelta_.total_seconds()\nassert total_seconds == 60 * 60 * 24 * 2 + 0.1\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7, millisecond=100)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\ntotal_seconds: ap.Number = timedelta_.total_seconds()\nassert total_seconds == 60 * 60 * 24 * 2 + 0.1\n```",  # noqa
    ##################################################
    "## total_seconds method API": "## total_seconds メソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get the total seconds in the duration.<hr>": "時間の間隔値の合計秒数を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `total_seconds`: Number": "- `total_seconds`: Number",
    ##################################################
    "  - Total seconds in the duration.": "  - 時間の間隔値の合計秒数。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\n>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 6)\n>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2\n>>> timedelta_.total_seconds()\nNumber(86400.0)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\n>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 6)\n>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2\n>>> timedelta_.total_seconds()\nNumber(86400.0)\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [TimeDelta class](https://simon-ritchie.github.io/apysc/en/timedelta.html)": "- [TimeDelta クラス](https://simon-ritchie.github.io/apysc/jp/jp_timedelta.html)",  # noqa
}
