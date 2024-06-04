"""This module is for the translation mapping data of the
following document:

Document file: datetime_day.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class day property": "# DateTime クラスの day 属性",
    ##################################################
    "This page explains the `DateTime` class's `day` property interface.": "このページでは`DateTime`クラスの`day`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `day` property gets or sets a day value.": "`day`属性では日の値の取得もしくは設定を行うことができます。",
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "A `DateTime` instance has its property interface.": "`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。",  # noqa
    ##################################################
    "Its getter interface returns a day's `Int` value.": "そのインターフェイスのgetterでは`Int`型の日の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\nday: ap.Int = datetime_.day\nassert day == 5\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\nday: ap.Int = datetime_.day\nassert day == 5\n```",  # noqa
    ##################################################
    "Also, its setter interface accepts a day's `Int` value.": "また、setterのインターフェイスでは同様に`Int`型の値を受け付けます。",  # noqa
    ##################################################
    "1-31 integer is acceptable.": "1～31の整数を受け付けることができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\ndatetime_.day = ap.Int(10)\nassert datetime_.day == 10\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\ndatetime_.day = ap.Int(10)\nassert datetime_.day == 10\n```",  # noqa
    ##################################################
    "## day property API": "## day 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current day's value.<hr>": "現在の日の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `day`: Int": "- `day`: Int",
    ##################################################
    "  - A current-day value.": "  - 現在の日の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\n>>> datetime_.day\nInt(1)\n\n>>> datetime_.day = ap.Int(2)\n>>> datetime_.day\nInt(2)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\n>>> datetime_.day\nInt(1)\n\n>>> datetime_.day = ap.Int(2)\n>>> datetime_.day\nInt(2)\n```",  # noqa
}
