"""This module is for the translation mapping data of the
following document:

Document file: datetime_month.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class month property": "# DateTime クラスの month 属性",
    ##################################################
    "This page explains the `DateTime` class's `month` property interface.": "このページでは`DateTime`クラスの`month`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `month` property gets or sets a month's value.": "`month`属性では月の値の取得もしくは設定を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "A `DateTime` instance has its property interface.": "`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。",  # noqa
    ##################################################
    "Its getter interface returns a month's `Int` value.": "そのgetterのインターフェイスは`Int`型の月の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\nassert datetime_.month == 12\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\nassert datetime_.month == 12\n```",  # noqa
    ##################################################
    "Also, its setter interface accepts a month's `Int` value.": "また、setter側のインターフェイスでは同様に`Int`型の月の値を受け付けます。",  # noqa
    ##################################################
    "1-12 integer is acceptable.": "1～12の範囲の整数を受け付けることができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\ndatetime_.month = ap.Int(1)\nassert datetime_.month == 1\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\ndatetime_.month = ap.Int(1)\nassert datetime_.month == 1\n```",  # noqa
    ##################################################
    "## month property API": "## month 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current month's value.<hr>": "現在の月の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `month`: Int": "- `month`: Int",
    ##################################################
    "  - A current month value.": "  - 現在の月の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\n>>> datetime_.month\nInt(12)\n\n>>> datetime_.month = ap.Int(1)\n>>> datetime_.month\nInt(1)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\n>>> datetime_.month\nInt(12)\n\n>>> datetime_.month = ap.Int(1)\n>>> datetime_.month\nInt(1)\n```",  # noqa
}
