"""This module is for the translation mapping data of the
following document:

Document file: datetime_minute.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class minute property": "# DateTime クラスの minute 属性",
    ##################################################
    "This page explains the `DateTime` class's `minute` property interface.": "このページでは`DateTime`クラスの`minute`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `minute` property gets or sets a minute value.": "`minute`属性では分の値の取得もしくは設定を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "A `DateTime` instance has its property interface.": "`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。",  # noqa
    ##################################################
    "Its getter interface returns a minute's `Int` value.": "そのインターフェイスのgetterでは`Int`型の分の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, minute=30)\nminute: ap.Int = datetime_.minute\nassert minute == 30\n```": "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, minute=30)\nminute: ap.Int = datetime_.minute\nassert minute == 30\n```",  # noqa
    ##################################################
    "Also, its setter interface accepts a minute's `Int` value.": "また、setter側のインターフェイスでは同様に`Int`型の分の値を受け付けます。",  # noqa
    ##################################################
    "0-59 integer is acceptable.": "0～59の整数を受け付けることができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, minute=30)\ndatetime_.minute = ap.Int(50)\nassert datetime_.minute == 50\n```": "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, minute=30)\ndatetime_.minute = ap.Int(50)\nassert datetime_.minute == 50\n```",  # noqa
    ##################################################
    "## minute property API": "## minute 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current minute's value.<hr>": "現在の分の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `minute`: Int": "- `minute`: Int",
    ##################################################
    "  - A current minute value.": "  - 現在の分の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, minute=30)\n>>> datetime_.minute\nInt(30)\n\n>>> datetime_.minute = ap.Int(50)\n>>> datetime_.minute\nInt(50)\n```": "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, minute=30)\n>>> datetime_.minute\nInt(30)\n\n>>> datetime_.minute = ap.Int(50)\n>>> datetime_.minute\nInt(50)\n```",  # noqa
}
