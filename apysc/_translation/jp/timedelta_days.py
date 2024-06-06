"""This module is for the translation mapping data of the
following document:

Document file: timedelta_days.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# TimeDelta class days interface": "# TimeDelta クラスの days インターフェイス",
    ##################################################
    "This page explains the `TimeDelta` class's `days` property interface.": "このページでは`TimeDelta`クラスの`days`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `days` property returns the number of days between two `DateTime` instances.": "`days`属性は2つの`DateTime`クラスのインスタンス間の日数値を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `days`' type is the apysc's `Int` and truncates a fraction value.": "`days`属性の値の型はapyscの`Int`型となり、且つその値の小数点数は切り捨てられます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\ndays: ap.Int = timedelta_.days\nassert days == 2\n\ndatetime_3: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_4: ap.DateTime = ap.DateTime(2022, 12, 5, hour=10)\ntimedelta_ = datetime_3 - datetime_4\ndays = timedelta_.days\nassert days == 1\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\ndays: ap.Int = timedelta_.days\nassert days == 2\n\ndatetime_3: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_4: ap.DateTime = ap.DateTime(2022, 12, 5, hour=10)\ntimedelta_ = datetime_3 - datetime_4\ndays = timedelta_.days\nassert days == 1\n```",  # noqa
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
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\n>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\n>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2\n>>> timedelta_.days\nInt(2)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\n>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\n>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2\n>>> timedelta_.days\nInt(2)\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [TimeDelta class](https://simon-ritchie.github.io/apysc/en/timedelta.html)": "- [TimeDelta クラス](https://simon-ritchie.github.io/apysc/jp/jp_timedelta.html)",  # noqa
}
