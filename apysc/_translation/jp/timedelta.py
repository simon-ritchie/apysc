"""This module is for the translation mapping data of the
following document:

Document file: timedelta.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# TimeDelta class": "# TimeDelta クラス",
    ##################################################
    "This page explains the `TimeDelta` class.": "このページでは`TimeDelta`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `TimeDelta` class treats a time delta between two `DateTime` instances.": "`TimeDelta`クラスは2つの`DateTime`クラスのインスタンス間の時間差を扱います。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Subtraction between two `DateTime` instances returns this class's instance.": "2つの`DateTime`クラスのインスタンス間の減算はこのクラスのインスタンスを返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\n```": "```py\n# runnable\nimport apysc as ap\n\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\n```",  # noqa
    ##################################################
    "A `TimeDelta` instance has each interface, such as the `days`' property or `total_seconds`' method, as follows:": "`TimeDelta`クラスのインスタンスは以下のように`days`属性や`total_seconds`メソッドなどの各インターフェイスを持っています:",  # noqa
    ##################################################
    "```\n# runnable\nimport apysc as ap\n\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\ndays: ap.Int = timedelta_.days\nassert days == 2\ntotal_seconds: ap.Number = timedelta_.total_seconds()\nassert total_seconds == 60 * 60 * 24 * 2\n```": "```\n# runnable\nimport apysc as ap\n\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\ndays: ap.Int = timedelta_.days\nassert days == 2\ntotal_seconds: ap.Number = timedelta_.total_seconds()\nassert total_seconds == 60 * 60 * 24 * 2\n```",  # noqa
    ##################################################
    "## days property API": "## days 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get days in the duration.<hr>": "時間の間隔値の日数を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `days`: Int": "- `days`: Int",
    ##################################################
    "  - Days value. This interface ignores a fraction.": "  - 日数値。小数点数の分は無視されます。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\n>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\n>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2\n>>> timedelta_.days\nInt(2)\n```": "```py\n>>> import apysc as ap\n>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\n>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\n>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2\n>>> timedelta_.days\nInt(2)\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [TimeDelta class days interface](https://simon-ritchie.github.io/apysc/en/timedelta_days.html)": "- [TimeDelta クラスの days インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_timedelta_days.html)",  # noqa
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
    "```py\n>>> import apysc as ap\n>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\n>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 6)\n>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2\n>>> timedelta_.total_seconds()\nNumber(86400.0)\n```": "```py\n>>> import apysc as ap\n>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\n>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 6)\n>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2\n>>> timedelta_.total_seconds()\nNumber(86400.0)\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [TimeDelta class total_seconds interface](https://simon-ritchie.github.io/apysc/en/timedelta_total_seconds.html)": "- [TimeDelta クラスの total_seconds インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_timedelta_total_seconds.html)",  # noqa
}
